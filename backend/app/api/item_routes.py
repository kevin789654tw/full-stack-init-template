from app.core.services.item_service import ItemService
from app.models.item import Item
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api", tags=["Items"])


@router.post("/items", response_model=Item)
def create_item(item: Item) -> Item:
    """
    Create a new item in the database.

    Args:
        item (Item): The Item object to be created.
                     'name' and 'description' cannot be empty or only whitespaces.

    Raises:
        HTTPException: If validation fails (400).

    Returns:
        Item: The newly created Item object.
    """
    try:
        return ItemService.create_item(item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/items", response_model=list[Item])
def get_items() -> list[Item]:
    """
    Retrieve all items from the database.

    Returns:
        list[Item]: A list of all Item objects.
    """
    return ItemService.list_items()


@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    """
    Retrieve a single item by its ID.

    Args:
        item_id (int): The ID of the item to retrieve.

    Raises:
        HTTPException: If the item with the given ID does not exist (404).

    Returns:
        Item: The Item object with the specified ID.
    """
    item = ItemService.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item) -> Item:
    """
    Update an existing item by its ID.

    Args:
        item_id (int): The ID of the item to update.
        item (Item): The updated Item data.
                     'name' and 'description' cannot be empty or only whitespaces.

    Raises:
        HTTPException: If the item does not exist (404) or validation fails (400).

    Returns:
        Item: The updated Item object.
    """
    existing_item = ItemService.get_item(item_id)
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    try:
        return ItemService.update_item(item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    """
    Delete an existing item by its ID.

    Args:
        item_id (int): The ID of the item to delete.

    Raises:
        HTTPException: If the item does not exist (404).

    Returns:
        dict: A confirmation message.
    """
    existing_item = ItemService.get_item(item_id)
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    ItemService.delete_item(existing_item)
    return {"detail": "Item deleted"}
