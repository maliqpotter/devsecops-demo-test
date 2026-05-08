import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from . import schemas, crud

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TODO App (FastAPI)")

# CORS
allow_origins = [o for o in os.getenv("ALLOW_ORIGINS", "").split(",") if o]
if allow_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Security Headers Middleware
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    return response

@app.get("/", tags=["health"])
def health():
    return {"status": "ok"}

@app.post("/tasks", response_model=schemas.TaskOut, status_code=201, tags=["tasks"])
def create_task(payload: schemas.TaskCreate, db: Session = Depends(get_db)):
    task = crud.create_task(db, payload)
    return task

@app.get("/tasks", response_model=list[schemas.TaskOut], tags=["tasks"])
def list_tasks(q: str | None = None, completed: bool | None = None, category: str | None = None, db: Session = Depends(get_db)):
    tasks = crud.list_tasks(db, q=q, completed=completed, category=category)
    return tasks

@app.get("/tasks/{task_id}", response_model=schemas.TaskOut, tags=["tasks"])
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.patch("/tasks/{task_id}", response_model=schemas.TaskOut, tags=["tasks"])
def update_task(task_id: int, payload: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    updated = crud.update_task(db, task, payload)
    return updated

@app.delete("/tasks/{task_id}", status_code=204, tags=["tasks"])
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, task)
    return None

@app.post("/tasks/{task_id}/toggle", response_model=schemas.TaskOut, tags=["tasks"])
def toggle_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.completed = not task.completed
    db.add(task)
    db.commit()
    db.refresh(task)
    return task
