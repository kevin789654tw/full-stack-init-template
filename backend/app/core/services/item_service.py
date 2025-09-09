from app.models.item import Item
from app.repositories.item_repository import ItemRepository


class ItemService:
    """Service layer handling operations and rules related to Items."""

    @staticmethod
    def _validate_item(item: Item) -> None:
        """
        Validate item name and description are not empty or whitespace.

        Args:
            item (Item): The Item instance to validate.

        Raises:
            ValueError: If the item name or description is empty or only whitespaces.

        Returns:
            None
        """
        if not item.name.strip():
            raise ValueError("Item name cannot be empty or only whitespaces")
        if not item.description.strip():
            raise ValueError("Item description cannot be empty or only whitespaces")

    @staticmethod
    def create_item(item: Item) -> Item:
        """
        Validate and create a new item via repository layer.

        Args:
            item (Item): The Item object to be created.

        Raises:
            ValueError: If the item name or description is empty or only whitespaces.

        Returns:
            Item: The newly created Item object.
        """
        ItemService._validate_item(item)
        return ItemRepository.create(item)

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
    def update_item(item: Item) -> Item:
        """
        Validate and update an existing item via repository layer.

        Args:
            item (Item): The Item object with updated data.

        Raises:
            ValueError: If the item name or description is empty or only whitespaces.

        Returns:
            Item: The updated Item object.
        """
        ItemService._validate_item(item)
        return ItemRepository.update(item)

    @staticmethod
    def delete_item(item: Item) -> None:
        """
        Delete an existing item via repository layer.

        Args:
            item (Item): The Item object to delete.

        Returns:
            None
        """
        ItemRepository.delete(item)
