from app.db.database import session
from app.models.item import Item
from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["Items"])


@router.get("/items", response_model=list[Item])
def get_items() -> list[Item]:
    with session() as db:
        return db.query(Item).all()


@router.post("/items", response_model=Item)
def create_item(item: Item) -> Item:
    with session() as db:
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
