"""
Example API endpoints
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class Item(BaseModel):
    id: int
    name: str
    description: str = None


# In-memory data store (replace with database in production)
items_db = [
    {"id": 1, "name": "Item 1", "description": "First item"},
    {"id": 2, "name": "Item 2", "description": "Second item"},
]


@router.get("/items")
async def get_items() -> List[Item]:
    """Get all items"""
    return items_db


@router.get("/items/{item_id}")
async def get_item(item_id: int) -> Item:
    """Get item by ID"""
    for item in items_db:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


@router.post("/items")
async def create_item(item: Item) -> Item:
    """Create new item"""
    items_db.append(item.dict())
    return item


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete item by ID"""
    global items_db
    items_db = [item for item in items_db if item["id"] != item_id]
    return {"message": "Item deleted"}
