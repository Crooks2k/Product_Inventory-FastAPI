from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from config.database import engine, Base

from middlewares.error_handler import Errorhandler
from routers.product import product_router
from routers.supplier import supplier_router
from routers.supplies import supplies_router

app = FastAPI()
app.title = "Proyecto de CRUD de inventario - FastAPI"
app.version = "0.0.1"
app.description = "Este proyecto es un ejemplo de una API RESTful desarrollada con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un modelo de inventariado \n Funcionalidades\n - Obtener los datos de los productos / proveedores\n - Obtener un producto / proveedore por su ID \n- Crear una nuevo producto / proveedor en el inventario \n- Actualizar una producto / proveedor existente\n - Eliminar un dato de proveedores o productos del inventario\n"

Base.metadata.create_all(bind=engine)


@app.get('/',tags=['home'],status_code=200)
def message():
    return HTMLResponse('<h1>Bienvenido al inventario.</h1>')

app.add_middleware(Errorhandler)
app.include_router(product_router)
app.include_router(supplier_router)
app.include_router(supplies_router)

