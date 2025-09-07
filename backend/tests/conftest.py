import os
import sys
from pathlib import Path
from typing import Iterator

import pytest
from app.db.database import Database
from sqlalchemy.engine import Engine
from sqlmodel import SQLModel

# add project root to sys.path to avoid import issues
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


@pytest.fixture(autouse=True)
def set_test_database_url(monkeypatch) -> None:
    """Automatically set a test DATABASE_URL for all tests."""
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")


@pytest.fixture(autouse=True)
def setup_db() -> Iterator[Engine]:
    """Setup and teardown the test database for the entire session."""
    os.getenv("DATABASE_URL")
    engine = Database.get_engine()

    SQLModel.metadata.create_all(engine)
    yield engine
    SQLModel.metadata.drop_all(engine)
