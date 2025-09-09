# Ignore Bandit warning B101 (assert used) in this file.
# For reference on usage, see:
# https://github.com/trunk-io/flake-factory/blob/275f85ee4ccb443fe7062ff8042bb1faf4d9935b/python/pytest/random_test.py#L1

# trunk-ignore-all(bandit/B101)
import pytest
from app.main import create_app
from fastapi.testclient import TestClient


@pytest.fixture()
def client():
    app = create_app()
    with TestClient(app) as c:
        yield c


def test_api_crud(client: TestClient) -> None:
    """Test CRUD operations of Item API endpoints."""

    # Create
    response = client.post(
        "/api/items",
        json={"name": "Test Item 01", "description": "Test Description 01"},
    )
    assert response.status_code == 200
    item_data = response.json()
    item_id = item_data["id"]
    assert item_data["name"] == "Test Item 01"

    # List all
    response = client.get("/api/items")
    assert response.status_code == 200
    assert any(it["id"] == item_id for it in response.json())

    # Read
    response = client.get(f"/api/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["id"] == item_id

    # Update
    response = client.put(
        f"/api/items/{item_id}",
        json={"name": "Test Item 02", "description": "Test Description 02"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item 02"

    # Delete
    response = client.delete(f"/api/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Item deleted"


def test_create_item_invalid_returns(client: TestClient) -> None:
    """POST /items should return 400 when name/description is invalid."""
    response = client.post("/api/items", json={"name": "   ", "description": ""})
    assert response.status_code == 400
    assert "cannot be empty" in response.json()["detail"]


def test_get_item_not_found_returns(client: TestClient) -> None:
    """GET /items/{id} should return 404 when item does not exist."""
    response = client.post(
        "/api/items", json={"name": "Test Name", "description": "Test Description"}
    )
    item_id = response.json()["id"]

    client.delete(f"/api/items/{item_id}")

    response = client.get(f"/api/items/{item_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_update_item_not_found_returns(client: TestClient) -> None:
    """PUT /items/{id} should return 404 when item does not exist."""
    response = client.put(
        "/api/items/9999", json={"name": "Test Name", "description": "Test Description"}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_update_item_invalid_returns(client: TestClient) -> None:
    """PUT /items/{id} should return 400 when updating with invalid data."""
    response = client.post(
        "/api/items", json={"name": "Test Name", "description": "Test Description"}
    )
    item_id = response.json()["id"]

    response = client.put(
        f"/api/items/{item_id}", json={"name": "   ", "description": ""}
    )
    assert response.status_code == 400
    assert "cannot be empty" in response.json()["detail"]


def test_delete_item_not_found_returns(client: TestClient) -> None:
    """DELETE /items/{id} should return 404 when item does not exist."""
    response = client.delete("/api/items/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"
