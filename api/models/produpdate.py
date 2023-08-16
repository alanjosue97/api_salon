from pydantic import BaseModel
from typing import Optional


class ProductUpdate(BaseModel):
    _id: str
    product_name: str


class AllUpdates(BaseModel):
    data: list[ProductUpdate]


