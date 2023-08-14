from pydantic import BaseModel
from typing import Optional

class CreateUsers(BaseModel):
    _id:str
    lastname:str  
    email:str
    
    
class ListUsers(BaseModel):
    data: list[CreateUsers]

class GetUserById(BaseModel):
    data: list[ListUsers]