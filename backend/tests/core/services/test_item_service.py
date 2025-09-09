# Ignore Bandit warning B101 (assert used) in this file.
# For reference on usage, see:
# https://github.com/trunk-io/flake-factory/blob/275f85ee4ccb443fe7062ff8042bb1faf4d9935b/python/pytest/random_test.py#L1

# trunk-ignore-all(bandit/B101)
import pytest
from app.core.services.item_service import ItemService
from app.models.item import Item

# fmt: off
invalid_item_data = [
    ("", "Valid Description", "Item name cannot be empty or only whitespaces"),
    ("   ", "Valid Description", "Item name cannot be empty or only whitespaces"),
    ("Valid Name", "", "Item description cannot be empty or only whitespaces"),
    ("Valid Name", "   ", "Item description cannot be empty or only whitespaces"),
    ("", "", "Item name cannot be empty or only whitespaces"),
]
# fmt: on


def test_item_service_crud() -> None:
    """Test CRUD operations of ItemService."""

    # Create
    item = Item(name="Test Name 01", description="Test Description 01")
    created_item = ItemService.create_item(item)
    assert created_item.id is not None
    assert created_item.name == "Test Name 01"
    assert created_item.description == "Test Description 01"

    # List all
    items = ItemService.list_items()
    assert any(i.id == created_item.id for i in items)

    # Read
    read_item = ItemService.get_item(created_item.id)
    assert read_item is not None
    assert read_item.name == "Test Name 01"
    assert read_item.description == "Test Description 01"

    # Update
    created_item.name = "Test Name 02"
    created_item.description = "Test Description 02"
    updated_item = ItemService.update_item(created_item)
    assert updated_item.id == created_item.id
    assert updated_item.name == "Test Name 02"
    assert updated_item.description == "Test Description 02"

    # Delete
    ItemService.delete_item(created_item)
    assert ItemService.get_item(created_item.id) is None


@pytest.mark.parametrize("name, description, expected_error", invalid_item_data)
def test_create_item_validation_errors(name, description, expected_error) -> None:
    """Test validation errors when creating Item with invalid values."""
    item = Item(name=name, description=description)

    with pytest.raises(ValueError) as exc_info:
        ItemService.create_item(item)
    assert str(exc_info.value) == expected_error


@pytest.mark.parametrize("new_name, new_description, expected_error", invalid_item_data)
def test_update_item_validation_errors(
    new_name, new_description, expected_error
) -> None:
    """Test validation errors when updating Item with invalid values."""
    item = Item(name="Valid Name", description="Valid Description")
    created_item = ItemService.create_item(item)

    created_item.name = new_name
    created_item.description = new_description

    with pytest.raises(ValueError) as exc_info:
        ItemService.update_item(created_item)
    assert str(exc_info.value) == expected_error
