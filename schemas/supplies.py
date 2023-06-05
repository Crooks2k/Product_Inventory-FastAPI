from pydantic import BaseModel, Field
from typing import Optional

class Supplies(BaseModel):
    id : Optional [int] 
    supplier_id : int = Field(ge=1)
    product_id : int = Field(ge=1)
    purchase_price : float = Field(ge=1)

    class Config:
        schema_extra = {
            "example":{
                'id': 1,
                'supplier_id': 1,
                'product_id': 1,                
                'purchase_price':1
            }
        }