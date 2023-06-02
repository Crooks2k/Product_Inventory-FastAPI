from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=30, min_length=3)
    brand: str = Field(max_length=300, min_length=3)
    description: str = Field(max_length=300, min_length=5)
    price: int = Field(ge=1, le=10000)
    availability: str = Field(max_length=30, min_length=3)
    avaliable_quantity: int = Field(ge=1, le=10000)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Iphone 13",
                "brand": "Apple",
                "description": "El iphone 13 es un telefono de gama alta por la empresa apple",
                "price": 1600,
                "availability": "disponible | no-disponible",
                "avaliable_quantity": 34,
            }
        }
