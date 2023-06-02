from models.product import Product as ProductModel
from schemas.product import Product

class ProductService():

    def __init__(self,db):
        self.db = db

    def get_product(self):
        """Use to get all products info (not require params)"""
        result = self.db.query(ProductModel).all()
        return result

    def get_product_by_id(self,id:int):
        """Use to get product info (need id: int with param)"""
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result    

    def add_product(self,product:Product):
        """Use to create products (need product: Product with params)"""

        existing_product = self.db.query(ProductModel).filter(ProductModel.id == product.id).first()
        if existing_product:
            return {"message": "Ya existe un producto con esa ID"}

        new_product = ProductModel(
            name=product.name,
            brand=product.brand,
            description=product.description,
            price=product.price,
            availability=product.availability,
            avaliable_quantity=product.avaliable_quantity
        )
        if new_product:
            self.db.add(new_product)
            self.db.commit()
            return {"message": "Producto inventariado correctamente"}
        


