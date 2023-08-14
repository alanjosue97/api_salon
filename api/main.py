from fastapi import FastAPI
from routes import products, categories, users



app = FastAPI()


app.include_router(products.router)
app.include_router(categories.router)
app.include_router(users.router)

@app.get("/healtcheck")
async def healtcheck():
    return {
       "healtcheck": "okat"
    }

     