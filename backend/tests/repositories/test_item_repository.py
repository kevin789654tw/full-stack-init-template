# Ignore Bandit warning B101 (assert used) in this file.
# For reference on usage, see:
# https://github.com/trunk-io/flake-factory/blob/275f85ee4ccb443fe7062ff8042bb1faf4d9935b/python/pytest/random_test.py#L1

# trunk-ignore-all(bandit/B101)
from app.models.item import Item
from app.repositories.item_repository import ItemRepository


def test_item_repository_crud() -> None:
    """Test CRUD operations of ItemRepository."""

    # Create
    item = Item(name="Test Name 01", description="Test Description 01")
    created_item = ItemRepository.create(item)
    assert created_item.id is not None
    assert created_item.name == "Test Name 01"
    assert created_item.description == "Test Description 01"

    # List all
    items = ItemRepository.list_all()
    assert any(i.id == created_item.id for i in items)

    # Read
    read_item = ItemRepository.get_by_id(created_item.id)
    assert read_item is not None
    assert read_item.name == "Test Name 01"
    assert read_item.description == "Test Description 01"

    # Update
    created_item.name = "Test Name 02"
    created_item.description = "Test Description 02"
    updated_item = ItemRepository.update(created_item)
    assert updated_item.id == created_item.id
    assert updated_item.name == "Test Name 02"
    assert updated_item.description == "Test Description 02"

    # Delete
    ItemRepository.delete(created_item)
    assert ItemRepository.get_by_id(created_item.id) is None
