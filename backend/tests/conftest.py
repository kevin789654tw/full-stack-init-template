import sys
from pathlib import Path
from typing import Iterator

import pytest
from app.db.database import Database
from dotenv import load_dotenv
from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel

# add project root to sys.path to avoid import issues
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# add test env variables
dotenv_path = ROOT_DIR / ".env.test"
load_dotenv(dotenv_path)


@pytest.fixture(autouse=True)
def setup_db(monkeypatch) -> Iterator[Engine]:
    """Setup and teardown the test database for the entire session."""
    engine = Database.get_engine()

    monkeypatch.setattr(Database, "get_engine", lambda: engine)

    SQLModel.metadata.create_all(engine)
    yield engine
    SQLModel.metadata.drop_all(engine)


@pytest.fixture()
def db_session() -> Iterator[Session]:
    """Provide a new database session for each test."""
    with Database.session() as s:
        yield s
