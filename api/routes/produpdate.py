from typing import Annotated
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, APIRouter
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.produpdate import ProductUpdate
from utils.database import get_db
from typing import List


router = APIRouter(
    prefix="/update",
    tags=["Update"],
)


@router.put("")
async def update_product_name(
    product_id: str,
    product_update: ProductUpdate,
    
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
):
    product_collection = database.get_collection("products")
    updated_product = await product_collection.find_one_and_update(
        {"_id": ObjectId(product_id)},
        {"$set": {"name": product_update.name}},
        return_document=ReturnDocument.AFTER
    )

    if updated_product:
        return {"message": "Product name updated successfully", "product": updated_product}
    else:
        return {"message": "Product not found"}

    

