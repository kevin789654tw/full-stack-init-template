from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.db.database import create_db_and_tables
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parents[2] / ".env"  # ./backend/
load_dotenv(dotenv_path=env_path, override=False)

# read from ./backend/.env
frontend_port = os.getenv("FRONTEND_PORT")

app = FastAPI(title="FastAPI Backend with SQLModel")

origins = [
    f"http://localhost:{frontend_port}",
    "https://your-frontend.com",   # change to your frontend url after deployment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# FastAPI automatically triggers the "startup" event when the app starts.
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(api_router)
