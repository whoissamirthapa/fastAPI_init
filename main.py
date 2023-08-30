from fastapi import FastAPI, Depends

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    res = {"item_id": item_id}
    return res

@app.get("/users/me")
async def read_user_me():
    res = {"user_id": "the current user"}
    return res

