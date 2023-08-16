from typing import Annotated
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, APIRouter
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.categories import CreateCategory

from utils.database import get_db


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post("")
async def create_category(
    create_category: CreateCategory,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
):
    users_data = create_category.dict(exclude_unset=True)
    users_data["_id"] = str(ObjectId())

    inserted_id = await database.categories.insert_one(users_data)

    return {"Category created successfully": "ok"}


@router.get("")
async def get_all_categories(
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]
):
    print(database.categories.find({}))
    all_categories = [categories async for categories in database.categories.find({})]

    return jsonable_encoder(all_categories)
