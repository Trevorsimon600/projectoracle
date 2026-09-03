from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import Session, select
from app.db import get_session
from app.models import Task
from app.services.prioritizer import score_task

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=Task)
def create_task(task: Task, session: Session = Depends(get_session)):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.get("/", response_model=List[Task])
def list_tasks(session: Session = Depends(get_session)):
    return session.exec(select(Task)).all()

@router.get("/recommendations", response_model=List[dict])
def recommend(session: Session = Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    scored = []
    for t in tasks:
        d = t.dict()
        s = score_task(d)
        d["score"] = s
        scored.append(d)
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored
