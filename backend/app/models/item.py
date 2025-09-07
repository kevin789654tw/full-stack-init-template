from sqlmodel import Field, SQLModel


# The class will automatically adds the table to `SQLModel.metadata`.
class Item(SQLModel, table=True):  # demonstration table
    """
    Database model representing an item.

    Attributes:
        id (int | None): Primary key of the item.
        name (str): Name of the item.
        description (str): Description of the item.
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
