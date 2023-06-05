from sqlalchemy import Column, Integer, Float,ForeignKey
from config.database import Base

class Supplies(Base):
    
    __tablename__ ="Supplies"

    id = Column(Integer, primary_key = True)
    product_id = Column(Integer, ForeignKey("Product.id"))
    supplier_id = Column(Integer, ForeignKey("Supplier.id"))
    purchase_price = Column(Float)