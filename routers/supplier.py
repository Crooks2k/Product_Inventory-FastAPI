from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from config.database import Session
from schemas.supplier import Supplier
from service.supplier import Supplier_Service

supplier_router = APIRouter()


@supplier_router.get(
    "/suppliers", tags=["Suppliers"], response_model=List[Supplier], status_code=200
)
def get_suppliers():
    db = Session()

    result = Supplier_Service(db).get_supplier()
    if not result:
        return JSONResponse(
            status_code=404,
            content={"message": "La lista de proveedores se encuentra vacia"},
        )
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@supplier_router.get("/supplier/{id}", tags=["Suppliers"], status_code=200)
def get_supplier(id: int):
    db = Session()

    result = Supplier_Service(db).get_supplier_by_id(id)
    if not result:
        return JSONResponse(
            status_code=404,
            content={"message": "No se encuentro ningun elemento con esa id"},
        )
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@supplier_router.post("/addsupplier/{id}", tags=["Suppliers"], status_code=200)
def new_supplier(supplier: Supplier):
    db = Session()

    result = Supplier_Service(db).add_supplier(supplier)
    if not result:
        return JSONResponse(
            status_code=500,
            content={"message": "Se encontro un error al crear el proveedor"},
        )
    if result == "Ya existe un proveedor con esa ID":
        return JSONResponse(status_code=409, content={"message": result})
    return JSONResponse(status_code=201, content={"message": result})


@supplier_router.put("/editsupplier/{id}", tags=["Suppliers"], status_code=200)
def edit_product(data: Supplier):
    db = Session()
    result = Supplier_Service(db).edit_supplier(data)
    if not result:
        return JSONResponse(
            status_code=500,
            content={"message": "Ocurrio un error al editar el producto"},
        )
    if result == "No existe un proveedor con esa ID, verifica el campo y vuelve a intentarlo":
        return JSONResponse(status_code=404, content={"message": result})
    return JSONResponse(status_code=200, content={"message": result})

@supplier_router.delete("/deletesupplier/{id}", tags=["Suppliers"], status_code=200)
def delete_supplier(id: int):
    db = Session()
    result = Supplier_Service(db).delete_supplier(id)
    if not result:
        return JSONResponse(
            status_code=500,
            content={"message": "Ocurrio un error al procesar la solicitud"}
        )
    if result == "No existe un proveedor con esa ID para eliminar, verifica el campo y vuelve a intentarlo":
        return JSONResponse(status_code=404, content={"message": result})
    return JSONResponse(status_code=200, content={"message": result})