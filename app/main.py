from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Sample Project",
    version="1.0.0",
    description="A simple FastAPI project to demonstrate clean structure."
)


class Item(BaseModel):
    id: int
    name: str
    price: float


# Fake in-memory database
items_db: dict[int, Item] = {}


@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}


@app.post("/items", response_model=Item)
def create_item(item: Item):
    """
    Create a new item and save it into the in-memory DB.
    """
    items_db[item.id] = item
    return item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """
    Retrieve an item by ID.
    """
    item = items_db.get(item_id)
    if not item:
        return {"error": "Item not found"}
    return item
