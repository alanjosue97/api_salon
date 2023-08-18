from pydantic import BaseModel
from typing import Optional


class CreateProduct(BaseModel):
    _id: str
    product_name: str
    brand: str
    category: str
    price: float
    presentation: str
    stock_available: float

class UpdateStock(BaseModel):
    quantity_change: float

class StockUpdateResponse(BaseModel):
    message: str
    new_stock_available: float
 
class ListProduct(BaseModel):
    id: str
    product_name: str
    brand: str
    category: str
    price: float
    presentation: str
    stock_available: float







