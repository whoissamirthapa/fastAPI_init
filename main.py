from fastapi import FastAPI, Depends
from pydantic import BaseModel
from src.dependency import depency_fun


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


def pass_depency(item: Item):
    return depency_fun(item.name, item.price)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/item")
async def create_item(item: Item, depency: str = Depends(pass_depency)):
    print("product" + item)
    return depency


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    res = {"item_id": item_id}
    return res


@app.get("/users/me")
async def read_user_me():
    res = {"user_id": "the current user"}
    return res
