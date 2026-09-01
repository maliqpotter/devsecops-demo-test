from datetime import datetime

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(None, max_length=255)
    description: str | None = Field(None, max_length=1000)
    completed: bool | None = None
    priority: str | None = Field("medium", pattern="^(low|medium|high)$")
    category: str | None = Field("general", max_length=50)


class TaskCreate(BaseModel):
    title: str = Field(..., max_length=255)
    description: str | None = Field(None, max_length=1000)
    priority: str | None = Field("medium", pattern="^(low|medium|high)$")
    category: str | None = Field("general", max_length=50)


class TaskUpdate(TaskBase):
    pass


class TaskOut(TaskBase):
    id: int
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True
