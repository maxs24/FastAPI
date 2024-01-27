from fastapi import APIRouter, Path

from models.model import Todo, TodoItem, TodoItems, ModelName
from typing import Any
todo_router = APIRouter()

todo_list = []


@todo_router.get('/files/{file_path:path}')  # :path указывает на то, что параметр должен соответствовать любому пути
async def file_path(file_path: str):
    return {"file_path": file_path}


@todo_router.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "detnet":  # Также можно получить через ModelName.detnet.value
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@todo_router.post('/todo')
async def add_todo(todo: TodoItem) -> dict:
    todo_list.append(todo)
    return {"Message": "Todo added successfuly"}


@todo_router.get('/todo', response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list
    }


@todo_router.get('/todo/{todo_id}')
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo with supplied ID doesn't exist."}


@todo_router.post('/todo/{todo_id}')
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully"}
    return {"message": "Todo with supplied ID doesn't exist."}


@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int = Path(..., title="The ID of the todo deleted")) -> dict:
    for index in range(len(todo_list)):
        if todo_list[index] == todo_id:
            todo_list.pop(index)
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo with supplied ID doesn't exist."}


@todo_router.delete("/todo")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {"message": "Todos deleted successfully"}
