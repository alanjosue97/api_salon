import os
 
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_INITDB_ROOT_USERNAME=os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD=os.getenv("MONGO_INITDB_ROOT_PASSWORD")

async def get_db():
    client = AsyncIOMotorClient(f"mongodb+srv://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@salon.ituskvf.mongodb.net/?retryWrites=true&w=majority")
    return client.control