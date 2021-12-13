from model import Todo

# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.TodoList
collection = database.todo


async def fetch_todo(title):
    todo = await collection.find_one({"title": title})
    return todo


async def fetch_todos():
    todos = []
    cursor = collection.find({})
    async for todo in cursor:
        todos.append(Todo(**todo))
    return todos


async def create_todo(todo):
    document = todo
    await collection.insert_one(document)
    return document


async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {
        "description": desc
    }})
    result = await collection.find_one({"title": title})
    return result


async def delete_todo(title):
    await collection.delete_one({"title": title})
    return True


