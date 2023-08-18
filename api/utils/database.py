import os

from motor.motor_asyncio import AsyncIOMotorClient

#MONGO_INITDB_ROOT_USERNAME=os.getenv("MONGO_INITDB_ROOT_USERNAME")
#MONGO_INITDB_ROOT_PASSWORD=os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGODB_URI = os.getenv("MONGODB_URI")


async def get_db():
    client = AsyncIOMotorClient(MONGODB_URI)
    #client = AsyncIOMotorClient(f"mongodb+srv://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@salon.ituskvf.mongodb.net/?retryWrites=true&w=majority")
  
    
    return client.control


# f"mongodb+srv://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@salon.ituskvf.mongodb.net/?retryWrites=true&w=majority"
