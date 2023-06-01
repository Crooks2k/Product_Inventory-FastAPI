from sqlalchemy import Column,Integer, String, Float

from config.database import Base


class Product(Base):

    __tablename__ = "Product"

    id = Column(Integer,primary_key = True)
    name = Column(String)
    brand = Column(String)
    description = Column(String)
    price = Column(Float)
    availability= Column(String)
    avaliable_quantity = Column(Integer)


