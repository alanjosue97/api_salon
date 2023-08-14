from pydantic import BaseModel
from typing import Optional

class CreateProduct(BaseModel):
    _id:str
    product_name:str  
    brand:str
    category:str
    price:float
    category:str
    presentation:str
    
    
class ListProduct(BaseModel):
    data: list[CreateProduct]