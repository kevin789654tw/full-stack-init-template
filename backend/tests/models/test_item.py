# Ignore Bandit warning B101 (assert used) in this file.
# For reference on usage, see:
# https://github.com/trunk-io/flake-factory/blob/275f85ee4ccb443fe7062ff8042bb1faf4d9935b/python/pytest/random_test.py#L1

# trunk-ignore-all(bandit/B101)
import pytest
from app.models.item import Item


def test_item_fields() -> None:
    """Test that Item fields are defined correctly."""
    item = Item(name="test_name", description="test_description")

    # init status (should be None before saving to DB)
    assert item.id is None
    # field type and value check
    assert isinstance(item.name, str)
    assert isinstance(item.description, str)
    assert item.name == "test_name"
    assert item.description == "test_description"


@pytest.mark.parametrize(
    "name, description",
    [
        ("test1", "desc1"),
        ("Test Name", "Test Description"),
    ],
)
def test_item_creation_parametrized(name, description) -> None:
    """Test creating Item with different values."""
    item = Item(name=name, description=description)
    assert item.name == name
    assert item.description == description
    assert item.id is None
