from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None
    priority: Optional[str] = Field("medium", pattern="^(low|medium|high)$")
    category: Optional[str] = Field("general", max_length=50)


class TaskCreate(BaseModel):
    title: str = Field(..., max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    priority: Optional[str] = Field("medium", pattern="^(low|medium|high)$")
    category: Optional[str] = Field("general", max_length=50)


class TaskUpdate(TaskBase):
    pass


class TaskOut(TaskBase):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True
