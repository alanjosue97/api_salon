from typing import Annotated
from fastapi import Header
from utils.database import get_db


async def validate_category(category: Annotated[str, Header()]):
    database = await get_db()

    category_exists = await database.categories.find_one({"category": category})
    print(category_exists)
    return True
