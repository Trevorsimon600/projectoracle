from fastapi import FastAPI
from app.db import create_db_and_tables
from app.routers import projects, tasks, uploads, recorder, notifications
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ORACLE MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(uploads.router)
app.include_router(recorder.router)
app.include_router(notifications.router)

@app.get("/")
def read_root():
    return {"message": "ORACLE backend running"}
