from enum import Enum
from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, title="The description of the item", max_length=300)
    price: float
    tax: float | None = Field(Field(gt=0, description="The price must be greater than zero"))

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "Example desc",
                    "price": 35.5,
                    "tax": 3.2,
                },
                {
                    "name": "Bar",
                    "price": "35.4",
                }
            ]
        }
    }


class User(BaseModel):
    username: str = Field(examples=["maxs24", "maxs2433"])
    full_name: str | None = Field(default=None, examples=["Максим"])


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
