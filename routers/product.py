from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from config.database import Session
from schemas.product import Product
from service.product import Product__Service


product_router = APIRouter()


@product_router.get(
    "/products", tags=["Products"], response_model=List[Product], status_code=200
)
def get_products():
    db = Session()

    result = Product__Service(db).get_product()
    if not result:
        return JSONResponse(
            status_code=404,
            content={"message": "La lista de productos se encuentra vacia"},
        )
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@product_router.get("/product/{id}", tags=["Products"], status_code=200)
def get_product(id: int):
    db = Session()

    result = Product__Service(db).get_product_by_id(id)
    if not result:
        return JSONResponse(
            status_code=404,
            content={"message": "No se encuentro ningun elemento con esa id"},
        )
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@product_router.post("/addproduct/{id}", tags=["Products"], status_code=200)
def new_product(product: Product):
    db = Session()

    result = Product__Service(db).add_product(product)
    if not result:
        return JSONResponse(
            status_code=500,
            content={"message": "Se encontro un error al crear el producto"},
        )
    if result == "Ya existe un producto con esa ID":
        return JSONResponse(status_code=409, content={"message": result})
    return JSONResponse(status_code=201, content={"message": result})


@product_router.put("/editproduct/{id}", tags=["Products"], status_code=200)
def edit_product(data: Product):
    db = Session()
    result = Product__Service(db).edit_product(data)
    if not result:
        return JSONResponse(
            status_code=500,
            content={"message": "Ocurrio un error al editar el producto"},
        )
    if result == "No existe un producto con esa ID, verifica el campo y vuelve a intentarlo":
        return JSONResponse(status_code=404, content={"message": result})
    return JSONResponse(status_code=200, content={"message": result})

@product_router.delete("/deleteproduct/{id}", tags=["Products"], status_code=200)
def delete_product(id: int):
    db = Session()
    result = Product__Service(db).delete_product(id)
    if not result:
        return JSONResponse(
            status_code=500,
            content={"message": "Ocurrio un error al procesar la solicitud"}
        )
    if result == "No existe un producto con esa ID para eliminar, verifica el campo y vuelve a intentarlo":
        return JSONResponse(status_code=404, content={"message": result})
    return JSONResponse(status_code=200, content={"message": result})