from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, APIRouter
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.products import CreateProduct, ListProduct, UpdateStock, StockUpdateResponse
from utils.database import get_db
from typing import List


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.post("")
async def create_products(
    create_products: CreateProduct,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
):
    print(get_db)
    
    print(create_products)
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
async def get_products_by_category(
    category: str,
    get_products_by_category: ListProduct,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
):
    # print(database.users.find_one({}))
    get_products_by_category = await database.products.find(
        {"category": category}
    ).to_list(length=None)

    return jsonable_encoder(get_products_by_category)

@router.post("/{product_id}")
async def get_product_by_id(
    product_id: str, 
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)]
):
    # print(database.users.find_one({}))
    product_id = await database.products.find_one({})

    return jsonable_encoder(product_id)

@router.put("/{product_id}/update_stock", response_model=StockUpdateResponse)
async def update_stock_product_by_id(
    product_id: str,
    update_stock: ListProduct,
    database: Annotated[AsyncIOMotorDatabase, Depends(get_db)],
):
    product = await database.products.find_one({})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    new_quantity = product["stock_available"] + update_stock.quantity_change
    await database.products.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": {"stock_available": new_quantity}}
    )

    return StockUpdateResponse(
        message="Stock updated successfully",
        new_stock_available=new_quantity
    )
    
@router.delete("/{product_id}")
async def delete_product(
    product_id: str,
    database: AsyncIOMotorDatabase = Depends(get_db)
):
    deleted_product = await database.CreateProduct.find_one_and_delete({"_id": product_id})
    
    if deleted_product:
        return {"message": "Product deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")