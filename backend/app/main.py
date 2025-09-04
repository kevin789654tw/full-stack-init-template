import os
from pathlib import Path

from app.api.item_routes import router as item_router
from app.db.database import create_db_and_tables
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

env_path = Path(__file__).resolve().parents[2] / ".env"  # ./backend/
load_dotenv(dotenv_path=env_path, override=False)

# read from ./backend/.env
FRONTEND_URL: str | None = os.getenv("FRONTEND_URL")

if FRONTEND_URL is None:
    raise ValueError("FRONTEND_URL not set")

app = FastAPI(title="FastAPI Backend with SQLModel")

origins = [
    FRONTEND_URL,
    # add URLs of other sub-frontends or environments
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


app.include_router(item_router)
