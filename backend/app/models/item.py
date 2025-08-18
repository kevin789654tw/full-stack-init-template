from sqlmodel import SQLModel, Field
from typing import Optional

# The class will automatically adds the table to `SQLModel.metadata`.
class Item(SQLModel, table=True):   # demonstration table
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
