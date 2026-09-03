import os
from uuid import uuid4
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "./data/uploads"))
VIDEO_DIR = Path(os.getenv("VIDEO_DIR", "./data/videos"))

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)

def save_upload_file(file, dest_dir: Path = UPLOAD_DIR) -> dict:
    ext = Path(file.filename).suffix
    fname = f"{uuid4().hex}{ext}"
    out_path = dest_dir / fname
    with open(out_path, "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename, "path": str(out_path), "stored_name": fname}

def save_video_file(file, dest_dir: Path = VIDEO_DIR) -> dict:
    # same logic as save_upload_file
    return save_upload_file(file, dest_dir)
