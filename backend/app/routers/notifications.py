from fastapi import APIRouter, BackgroundTasks
from app.services.notifier import send_sms

router = APIRouter(prefix="/notify", tags=["notify"])

@router.post("/sms")
def notify_sms(number: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_sms, number, message)
    return {"status": "queued"}
