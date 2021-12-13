from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

# App object
app = FastAPI()

from database import (
    fetch_todo,
    fetch_todos,
    create_todo,
    update_todo,
    delete_todo
)

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_roo():
    return {"data": "Hello, World"}


@app.get("/api/todo")
async def get_todos():
    response = await fetch_todos()
    return response


@app.get("/api/todo{title}", response_model=Todo)
async def get_todo(title):
    response = await fetch_todo(title)
    if response:
        return response
    raise HTTPException(404, f"no todo with title {title}")


@app.post("/api/todo", response_model=Todo)
async def create_todo(todo:Todo):
    # print(todo.dict())
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "something went wrong")


@app.put("/api/todo{id}", response_model=Todo)
async def update_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"there is no todo with title: {title}")


@app.delete("/api/todo{title}")
async def delete_todo(title):
    response = await delete_todo(title)
    if response:
        return "successfully deleted the todo"
    raise HTTPException(404, f"there is no todo with title: {title}")
