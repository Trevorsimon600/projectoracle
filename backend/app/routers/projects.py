from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import Session, select
from app.db import get_session
from app.models import Project

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=Project)
def create_project(project: Project, session: Session = Depends(get_session)):
    session.add(project)
    session.commit()
    session.refresh(project)
    return project

@router.get("/", response_model=List[Project])
def list_projects(session: Session = Depends(get_session)):
    projects = session.exec(select(Project)).all()
    return projects

@router.get("/{project_id}", response_model=Project)
def get_project(project_id: int, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
