
from typing import Optional
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None

class TaskCreate(BaseModel):
    title: str = Field(..., max_length=255)
    description: Optional[str] = Field(None, max_length=1000)

class TaskUpdate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True
