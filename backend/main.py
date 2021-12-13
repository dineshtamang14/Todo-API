from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# App object
app = FastAPI()

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
    return 1


@app.get("/api/todo{id}")
async def get_todo(id):
    return 1


@app.post("/api/todo")
async def create_todo(todo):
    return 1


@app.put("/api/todo{id}")
async def update_todo(id, data):
    return 1


@app.delete("/api/todo{id}")
async def delete_todo(id):
    return 1
