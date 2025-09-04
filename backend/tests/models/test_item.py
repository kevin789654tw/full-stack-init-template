# Ignore Bandit warning B101 (assert used) in this file.
# For reference on usage, see:
# https://github.com/trunk-io/flake-factory/blob/275f85ee4ccb443fe7062ff8042bb1faf4d9935b/python/pytest/random_test.py#L1

# trunk-ignore-all(bandit/B101)
import pytest
from app.models.item import Item
from sqlmodel import Session, SQLModel


def test_item_fields():
    """Test that Item fields are defined correctly."""
    item = Item(name="test_name", description="test_description")

    # init status (should be None before saving to DB)
    assert item.id is None
    # field type and value check
    assert isinstance(item.name, str)
    assert isinstance(item.description, str)
    assert item.name == "test_name"
    assert item.description == "test_description"


def test_item_table_registered():
    """Test that Item is registered in SQLModel metadata."""
    tables = SQLModel.metadata.tables

    # table name check (automatically turn class name into lower case)
    assert "item" in tables
    item_table = tables["item"]

    # exist columns check
    assert "id" in item_table.c
    assert "name" in item_table.c
    assert "description" in item_table.c

    # primary key check
    assert item_table.c.id.primary_key is True


@pytest.mark.parametrize(
    "name, description",
    [
        ("test1", "desc1"),
        ("Test Name", "Test Description"),
    ],
)
def test_item_creation_parametrized(name, description):
    """Test creating Item with different values."""
    item = Item(name=name, description=description)
    assert item.name == name
    assert item.description == description
    assert item.id is None


def test_item_crud(db_session: Session) -> None:
    """Test full CRUD (Create, Read, Update, Delete) operations for Item."""
    # Create
    item = Item(name="Test Item 01", description="Test Description")
    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)

    assert item.id is not None

    # Read
    db_item = db_session.get(Item, item.id)
    assert db_item.name == "Test Item 01"
    assert db_item.description == "Test Description"

    # Update
    db_item.name = "Test Item 02"
    db_session.add(db_item)
    db_session.commit()
    db_session.refresh(db_item)

    assert db_item.name == "Test Item 02"

    # Delete
    db_session.delete(db_item)
    db_session.commit()
    assert db_session.get(Item, db_item.id) is None


def test_get_items(db_session: Session) -> None:
    """Test retrieving multiple Item instances from the database."""
    # empty check
    items = db_session.query(Item).all()
    assert items == []

    # create multiple items
    items_to_create = [
        Item(name=f"Test Item {i}", description=f"Test Description {i}")
        for i in range(3)
    ]
    db_session.add_all(items_to_create)
    db_session.commit()

    # retrieve all items
    items = db_session.query(Item).all()
    assert len(items) == 3
    for i, item in enumerate(items):
        assert item.name == f"Test Item {i}"
        assert item.description == f"Test Description {i}"
