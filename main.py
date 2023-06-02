from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from config.database import engine, Base

from middlewares.error_handler import Errorhandler
from routers.product import product_router


app = FastAPI()
app.title = "Inventario FastAPI"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)



app.add_middleware(Errorhandler)
app.include_router(product_router)