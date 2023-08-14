from motor.motor_asyncio import AsyncIOMotorClient

async def get_db():
    client = AsyncIOMotorClient("mongodb+srv://salon:Salon123@salon.ituskvf.mongodb.net/?retryWrites=true&w=majority")
    return client.control