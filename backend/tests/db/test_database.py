# Ignore Bandit warning B101 (assert used) in this file.
# For reference on usage, see:
# https://github.com/trunk-io/flake-factory/blob/275f85ee4ccb443fe7062ff8042bb1faf4d9935b/python/pytest/random_test.py#L1

# Import Item only to ensure it is registered in SQLModel metadata.
# The table definition is needed for create_db_and_tables(), even if unused here.

# trunk-ignore-all(bandit/B101)
from app.db.database import Database
from app.models.item import Item  # noqa: F401
from sqlmodel import inspect


def test_item_table_registered(setup_db) -> None:
    """Test that Item table is actually created in a test database."""
    engine = setup_db
    Database.create_db_and_tables(custom_engine=engine)
    inspector = inspect(engine)

    # table name check (automatically turn class name into lower case)
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
