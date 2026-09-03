from fastapi import APIRouter, UploadFile, File, Depends
from sqlmodel import Session
from app.db import get_session
from app.services.storage import save_video_file
from app.models import VideoLog

router = APIRouter(prefix="/recorder", tags=["recorder"])

@router.post("/video")
async def upload_video(file: UploadFile = File(...), project_id: int = None, notes: str = None, session: Session = Depends(get_session)):
    saved = save_video_file(file)
    vlog = VideoLog(filename=saved["filename"], path=saved["path"], notes=notes, project_id=project_id)
    session.add(vlog)
    session.commit()
    session.refresh(vlog)
    return {"video": vlog}
