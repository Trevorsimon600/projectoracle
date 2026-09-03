from fastapi import APIRouter, UploadFile, File, Depends
from sqlmodel import Session
from app.db import get_session
from app.services.storage import save_upload_file
from app.models import Upload

router = APIRouter(prefix="/uploads", tags=["uploads"])

@router.post("/")
async def upload_file(file: UploadFile = File(...), project_id: int = None, session: Session = Depends(get_session)):
    saved = save_upload_file(file)
    upload = Upload(filename=saved["filename"], path=saved["path"], content_type=file.content_type, project_id=project_id)
    session.add(upload)
    session.commit()
    session.refresh(upload)
    return {"upload": upload}
