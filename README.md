# ControlProduct
## Initial setup FastAPI

Initialize the Poetry and add its requirements:

```bash
poetry init
poetry add fastapi
poetry add uvicorn[standard]
poetry add motor
```

## FastApi + MongoDB

```bash
docker run --name database-api 
    -e MONGO_INITDB_ROOT_USERNAME=salon 
    -e MONGO_INITDB_ROOT_PASSWORD=Salon123 
    -e MONGO_INITDB_DATABASE=test 
    -p 27017:27017 
    -d mongo:latest

```

## Database

```bash
cd db
docker build -t salon-control-db .
docker run -p 27017:27017 -d salon-control-db
```

## API

```bash
cd api
docker build -t salon-api .
docker run -p 8000:8000 -d salon-api
```
