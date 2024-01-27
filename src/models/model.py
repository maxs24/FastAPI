from enum import Enum
from pydantic import BaseModel
from typing import List, Optional


class ModelName(str, Enum):
    # Перечисление Enum, первый класс наследник определяет какого типа должны быть элементы
    alexnet = 'alexnet'
    detnet = 'detnet'



class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example value": {
                "id": 1,
                "item": "Example text"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Прочитать следующую главу книги."
            }
        }


class TodoItems(BaseModel):
    items: Optional[List[TodoItem]]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Прочитать следующую главу книги."
                    },
                    {
                        "item": "Example 2"
                    }
                ]
            }
        }
