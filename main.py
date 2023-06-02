from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from config.database import engine, Base

from middlewares.error_handler import Errorhandler
from routers.product import product_router


app = FastAPI()
app.title = "Proyecto de CRUD de inventario - FastAPI"
app.version = "0.0.1"
app.description = "Este proyecto es un ejemplo de una API RESTful desarrollada con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un modelo de inventariado \n Funcionalidades\n - Obtener los datos de los productos\n - Obtener un producto por su ID \n- Crear una nuevo producto en el inventario \n- Actualizar una producto existente\n - Eliminar un item del inventario\n"

Base.metadata.create_all(bind=engine)


@app.get('/',tags=['home'],status_code=200)
def message():
    return HTMLResponse('<h1>Bienvenido al inventario.</h1>')

app.add_middleware(Errorhandler)
app.include_router(product_router)

