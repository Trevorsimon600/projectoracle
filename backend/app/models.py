from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    display_name: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    status: Optional[str] = "active"
    priority: Optional[int] = 5
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Goal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    title: str
    description: Optional[str] = None
    parent_id: Optional[int] = None
    level: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    title: str
    description: Optional[str] = None
    importance: int = 5
    urgency: int = 5
    effort: int = 5
    status: str = "todo"
    dependencies: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Upload(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str
    path: str
    content_type: Optional[str] = None
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)

class VideoLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str
    path: str
    duration_seconds: Optional[int] = None
    notes: Optional[str] = None
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)
