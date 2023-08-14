from typing import Annotated
import secrets
from bson import ObjectId
import uuid
from uuid import uuid4
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, APIRouter
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.users import CreateUsers, ListUsers, GetUserById

from utils.database import get_db


 
router = APIRouter(
    prefix="/users",
    tags= [
        "Users"
    ],

)

@router.post("")
async def create_users(create_users:CreateUsers, database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    users_data = create_users.dict(exclude_unset=True)
    users_data["_id"] = str(ObjectId())
    users_data["token"] = secrets.token_hex(12)
    
    inserted_id = await database.users.insert_one(users_data)
    
    return {"Users created successfully": inserted_id.inserted_id} 
        

@router.post("/{user_id}")
async def get_users_by_id(user_id:str, database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    #print(database.users.find_one({}))
    user = await database.users.find_one({})

    return jsonable_encoder(user)

@router.get("")
async def list_users( database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    print(database.users.find({}))
    list_users = [users async for users in database.users.find({})]

    return jsonable_encoder(list_users)
    
   