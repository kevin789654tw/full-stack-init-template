from sqlmodel import Field, SQLModel


# The class will automatically adds the table to `SQLModel.metadata`.
class Item(SQLModel, table=True):  # demonstration table
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
