from sqlmodel import SQLModel, Session, create_engine
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parents[2] / ".env"  # ./backend/
load_dotenv(dotenv_path=env_path, override=False)

# read from docker-compose service's env_file
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def session():
    return Session(engine)
