import os
from pathlib import Path

from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine

env_path = Path(__file__).resolve().parents[2] / ".env"  # ./backend/
load_dotenv(dotenv_path=env_path, override=False)

# read from docker-compose service's env_file
DATABASE_URL: str | None = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL not set")

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def session() -> Session:
    return Session(engine)
