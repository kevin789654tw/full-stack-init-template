from app.db.database import session
from app.models.item import Item


class ItemRepository:
    """Repository layer for Item database operations."""

    @staticmethod
    def list_all() -> list[Item]:
        """
        Retrieve all items from the database.

        Returns:
            list[Item]: A list of all Item objects.
        """
        with session() as db:
            return db.query(Item).all()

    @staticmethod
    def get_by_id(item_id: int) -> Item | None:
        """
        Retrieve a single item by its ID.

        Args:
            item_id (int): The ID of the item to retrieve.

        Returns:
            Item | None: The Item object if found, otherwise None.
        """
        with session() as db:
            return db.query(Item).filter(Item.id == item_id).first()

    @staticmethod
    def create(item: Item) -> Item:
        """
        Create a new item in the database.

        Args:
            item (Item): The Item object to be created.

        Returns:
            Item: The newly created Item object.
        """
        with session() as db:
            db.add(item)
            db.commit()
            db.refresh(item)
            return item

    @staticmethod
    def update(item: Item) -> Item:
        """
        Update an existing item in the database.

        Args:
            item (Item): The Item object with updated data.

        Returns:
            Item: The updated Item object.
        """
        with session() as db:
            db.merge(item)
            db.commit()
            return item

    @staticmethod
    def delete(item: Item):
        """
        Delete an existing item from the database.

        Args:
            item (Item): The Item object to delete.

        Returns:
            None
        """
        with session() as db:
            db.delete(item)
            db.commit()
