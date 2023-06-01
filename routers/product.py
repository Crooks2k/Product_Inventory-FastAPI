from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from config.database import Session
from schemas.product import Product
from service.product import ProductService


product_router = APIRouter()


@product_router.get("/products", tags=["Products"], response_model=List[Product], status_code=200)
def get_products():
    db = Session()
    try:
        result = ProductService(db).get_product()
        return JSONResponse(content=jsonable_encoder(result), status_code=200)
    except Exception as e:
        return JSONResponse(content=jsonable_encoder(e), status_code=500)

@product_router.get("/product/{id}", tags=["Products"], status_code=200)
def get_product(id: int):
    db = Session()
    try:
        result = ProductService(db).get_product(id)
        return JSONResponse(content=jsonable_encoder(result), status_code=200)
    except Exception as e:
        return JSONResponse(content=jsonable_encoder(e), status_code=500)

@product_router.post("/addproduct/{id}", tags=["Products"], status_code=200)
def new_product(product: Product):
    db = Session()
    try:
        result = ProductService(db).add_product(product)
        return JSONResponse(status_code=404,content={"message": result})
    except Exception as e:
        return JSONResponse(content=jsonable_encoder(e), status_code=500)
