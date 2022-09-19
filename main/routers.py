from typing import Optional
from fastapi import APIRouter, Request 
from main import contracts

router = APIRouter()

@router.get("/")
def hello():
    return {"hello world"}

#path parametre
@router.get("/items/{item_id}")
async def item(item_id: int):
    return({"item_id": item_id})

#query parametre
@router.get("/users/", description="{user_id} is required. x is optional")
async def users(user_id: str, x: Optional[str] = None):
    if x:
        return{"item_id": user_id, "x": x}
    return{"item_id": user_id}

#response body parametre
@router.post("/items/")
async def create_item(item: contracts.Item):
    item_dict = item.dict()
    return item_dict