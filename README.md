# ORACLE — Personal Intelligence System (MVP)

Overview
--------
This is a minimal ORACLE v0.1 scaffold:
- Backend: FastAPI + SQLModel (SQLite)
- Frontend: React + Vite
- Local file storage for uploads and recorded videos
- Roadmap editor (Markdown outline → structured data)
- Simple prioritizer ("What should I work on?")
- Notifications: Browser notifications (and Twilio SMS stub if configured)

Quick start (recommended, local)
--------------------------------
1. Clone the repo and open the projectoracle directory.
2. Backend:
   - cd backend
   - python -m venv .venv
   - source .venv/bin/activate   (macOS/Linux) or .venv\Scripts\activate (Windows)
   - pip install -r requirements.txt
   - cp .env.example .env and update if needed
   - mkdir -p data/uploads data/videos
   - uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

3. Frontend:
   - cd frontend
   - npm install
   - npm run dev
   - Visit http://localhost:5173

Notes
-----
- SQLite DB file path: backend/data/oracle.db
- Uploads saved to backend/data/uploads, videos saved to backend/data/videos
- To enable Twilio SMS notifications, set TWILIO_SID, TWILIO_TOKEN, TWILIO_FROM in backend/.env
- The prioritizer is intentionally simple; extend services/prioritizer.py for more advanced scoring.

Project layout
--------------
projectoracle/
  backend/
    app/
      main.py
      db.py
      models.py
      routers/
        projects.py
        goals.py
        tasks.py
        uploads.py
        recorder.py
        notifications.py
      services/
        storage.py
        notifier.py
        prioritizer.py
    requirements.txt
    .env.example
  frontend/
    package.json
    vite.config.js
    index.html
    src/
      main.jsx
      App.jsx
      pages/
        Home.jsx
        RoadmapEditor.jsx
        Recorder.jsx
      components/
        VideoRecorder.jsx
        UploadForm.jsx
      styles.css
  README.md

Security & next steps
---------------------
- Add authentication (JWT / OAuth).
- Add background job worker for heavy tasks (transcription).
- Add tests and CI.
