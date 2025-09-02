import sys
from pathlib import Path

import pytest
from sqlmodel import Session, SQLModel, create_engine

# add project root to sys.path to avoid import issues
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# test database setup
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, echo=False)


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    """Create and drop tables for the test session."""
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)


@pytest.fixture()
def db_session():
    """Provide a database session for each test."""
    with Session(engine) as s:
        yield s
