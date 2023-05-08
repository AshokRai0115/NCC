from typing import Union
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/api/v1/post/all")
def read_all_posts():
    file = open("./data/Post.json")
    content = json.load(file)
    # posts = Post.all();
    # return ({
    #     "message": "Read successfully",
    #     "status": "success",
    #     data: posts
    # })
    return content

@app.get("/api/v1/user/all")
def read_all_users():
    file = open("./data/User.json")
    content = json.load(file)
    # posts = Post.all();
    # return ({
    #     "message": "Read successfully",
    #     "status": "success",
    #     data: posts
    # })
    return content