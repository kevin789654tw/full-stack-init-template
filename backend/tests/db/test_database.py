# Ignore Bandit warning B101 (assert used) in this file.
# For reference on usage, see:
# https://github.com/trunk-io/flake-factory/blob/275f85ee4ccb443fe7062ff8042bb1faf4d9935b/python/pytest/random_test.py#L1

# Import Item only to ensure it is registered in SQLModel metadata.
# The table definition is needed for create_db_and_tables(), even if unused here.

# trunk-ignore-all(bandit/B101)
import pytest
from app.db.database import Database
from app.models.item import Item  # noqa: F401
from sqlalchemy.pool import StaticPool
from sqlmodel import inspect


def test_get_database_url(monkeypatch):
    """Test DATABASE_URL retrieval and missing value error."""
    # success
    assert Database.get_database_url() == "sqlite:///:memory:"

    # missing
    monkeypatch.delenv("DATABASE_URL", raising=False)
    with pytest.raises(ValueError, match="DATABASE_URL not set"):
        Database.get_database_url()


def test_get_engine_behavior(monkeypatch):
    """Test behavior of different TEST_MODE settings and singleton engine."""
    Database._engine = None

    monkeypatch.setenv("TEST_MODE", "False")
    engine1 = Database.get_engine()
    engine2 = Database.get_engine()
    assert engine1 is engine2  # singleton check

    monkeypatch.setenv("TEST_MODE", "True")
    engine3 = Database.get_engine()
    assert engine3 is engine1  # singleton check

    Database._engine = None
    monkeypatch.setenv("TEST_MODE", "True")
    engine4 = Database.get_engine()
    assert isinstance(engine4.pool, StaticPool)


def test_item_table_registered(setup_db) -> None:
    """Test that Item table is actually created in a test database."""
    # default engine check
    Database._engine = None
    Database.create_db_and_tables()
    inspector = inspect(Database.get_engine())
    assert "item" in inspector.get_table_names()

    # custom engine check
    engine = setup_db
    Database.create_db_and_tables(custom_engine=engine)
    inspector = inspect(engine)
    assert "item" in inspector.get_table_names()

    # columns check
    columns = [c["name"] for c in inspector.get_columns("item")]
    expected_columns = ["id", "name", "description"]
    for col in expected_columns:
        assert col in columns

    # primary key check
    pk_info = inspector.get_pk_constraint("item")
    assert pk_info["constrained_columns"] == ["id"]


def test_session_can_connect(db_session) -> None:
    """Test that session can be created and connected to the database."""
    assert db_session is not None
    assert db_session.bind is not None
