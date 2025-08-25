
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas

def create_task(db: Session, data: schemas.TaskCreate) -> models.Task:
    task = models.Task(title=data.title, description=data.description or None)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def list_tasks(db: Session, q: Optional[str] = None, completed: Optional[bool] = None) -> List[models.Task]:
    stmt = select(models.Task)
    if q:
        q_like = f"%{q}%"
        stmt = stmt.where(models.Task.title.like(q_like))
    if completed is not None:
        stmt = stmt.where(models.Task.completed == completed)
    stmt = stmt.order_by(models.Task.id.desc())
    return list(db.execute(stmt).scalars().all())

def get_task(db: Session, task_id: int) -> Optional[models.Task]:
    return db.get(models.Task, task_id)

def update_task(db: Session, task: models.Task, data: schemas.TaskUpdate) -> models.Task:
    if data.title is not None:
        task.title = data.title
    if data.description is not None:
        task.description = data.description
    if data.completed is not None:
        task.completed = data.completed
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task: models.Task) -> None:
    db.delete(task)
    db.commit()
