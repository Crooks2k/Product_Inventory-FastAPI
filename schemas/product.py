from pydantic import BaseModel, Field
from typing import Optional 

class Product(BaseModel):
        id: Optional[int] = None
        name: str = Field(max_length=30,min_length=3)
        brand: str = Field(max_length=300,min_length=3)
        description: str = Field(max_length=300,min_length=10)
        price: int = Field(ge=1,le=10000)
        availability : str  = Field(max_length=15,min_length=3)
        avaliable_quantity: int = Field(ge=1, le=10000)

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'name': 'Nombre producto',
                    'brand': "Marca producto",
                    'description': "Descripción del producto",
                    'price': 1400,
                    'availability':'disponible | no-disponible',
                    'avaliable_quantity': 34,
                }
            }

