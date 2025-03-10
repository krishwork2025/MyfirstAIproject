from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = "sai"):
    return {"item_id": item_id, "q": q}

@app.get("/item/{q}")
def read_item(item_id: Union[int, None] = None, q: Union[str, None] = None, sex: Union[bool, None] = None):
    return { "q": q, "sex": sex}