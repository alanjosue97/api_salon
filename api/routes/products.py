from typing import Annotated
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, APIRouter
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.products import CreateProduct, ListProduct
from utils.database import get_db
from typing import List


 
router = APIRouter(
    prefix="/products",
    tags= [
        "Products"
    ],

)

@router.post("")
async def create_products(create_products:CreateProduct, database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    product_data = create_products.dict(exclude_unset=True)
    product_data["_id"] = str(ObjectId())
    
    inserted_id = await database.products.insert_one(product_data)
    
    return {"Product created successfully": inserted_id.inserted_id}
        

@router.get("")
async def list_products(database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    print(database.products.find({}))
    list_product = [products async for products in database.products.find({})]

    return jsonable_encoder(list_product)
    

@router.post("/category/{category}")
async def get_products_by_category(category:str, get_products_by_category:ListProduct, database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    #print(database.users.find_one({}))
    get_products_by_category = await database.products.find({"category": category}).to_list(length=None)

    return jsonable_encoder(get_products_by_category)