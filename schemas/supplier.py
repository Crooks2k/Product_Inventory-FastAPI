from pydantic import BaseModel, Field
from typing import Optional


class Supplier(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=100, min_length=3)
    address: str = Field(max_length=100, min_length=3)
    phone: int = Field(ge=1, le=9999999999)
    email: str = Field(max_length=100, min_length=3)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Carlitos Molina",
                "address": "Kr 11D 54-40sur",
                "phone": 320347840,
                "email": "example@gmail.com"
            }
        }
