from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from .database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(String(1000), nullable=True)
    completed = Column(Boolean, default=False, index=True)
    priority = Column(String(20), default="medium")  # low, medium, high
    category = Column(String(50), default="general")
    created_at = Column(DateTime, default=datetime.utcnow)
