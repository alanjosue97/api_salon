from pydantic import BaseModel
from typing import Optional

class CreateCategory(BaseModel):
    _id:str
    category_name: str

class AllCategories(BaseModel):
    data: list[CreateCategory]

class GetCategoriesByName(BaseModel):
    data: list[AllCategories]