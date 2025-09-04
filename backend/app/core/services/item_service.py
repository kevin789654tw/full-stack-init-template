from app.models.item import Item
from app.repositories.item_repository import ItemRepository


class ItemService:
    """Service layer for Item business logic."""

    @staticmethod
    def list_items() -> list[Item]:
        """
        Retrieve all items via repository layer.

        Returns:
            list[Item]: A list of all Item objects.
        """
        return ItemRepository.list_all()

    @staticmethod
    def get_item(item_id: int) -> Item | None:
        """
        Retrieve a single item by ID via repository layer.

        Args:
            item_id (int): The ID of the item to retrieve.

        Returns:
            Item | None: The Item object if found, otherwise None.
        """
        return ItemRepository.get_by_id(item_id)

    @staticmethod
    def create_item(item: Item) -> Item:
        """
        Create a new item via repository layer.

        Args:
            item (Item): The Item object to be created.

        Returns:
            Item: The newly created Item object.
        """
        return ItemRepository.create(item)

    @staticmethod
    def update_item(item: Item) -> Item:
        """
        Update an existing item via repository layer.

        Args:
            item (Item): The Item object with updated data.

        Returns:
            Item: The updated Item object.
        """
        return ItemRepository.update(item)

    @staticmethod
    def delete_item(item: Item):
        """
        Delete an existing item via repository layer.

        Args:
            item (Item): The Item object to delete.
        """
        ItemRepository.delete(item)
