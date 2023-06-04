from sqlalchemy import Column,Integer, String, Float

from config.database import Base


class Supplier(Base):

    __tablename__ = "Supplier"

    id = Column(Integer,primary_key = True)
    name = Column(String)
    address = Column(String)
    phone = Column(Integer)
    email= Column(String)


