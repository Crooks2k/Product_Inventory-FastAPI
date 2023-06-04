from models.product import Product as ProductModel
from schemas.product import Product

class Product__Service():

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
            return "Ya existe un producto con esa ID"

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
            return "Producto inventariado correctamente"
        
    def edit_product(self, data: Product):
        """Use to edit products (need two params => id: int || product: Product)"""
        product_exist: Product = self.db.query(ProductModel).filter(ProductModel.id == data.id).first()
        if not product_exist:
            return "No existe un producto con esa ID, verifica el campo y vuelve a intentarlo"
        
        product_exist.name = data.name
        product_exist.brand = data.brand
        product_exist.description = data.description
        product_exist.price = data.price
        product_exist.availability = data.availability
        product_exist.avaliable_quantity = data.avaliable_quantity
        self.db.commit()
        
        return "El producto fue editado correctamente"

    def delete_product(self, id: int):
        """Use to deleted product, need one param => id: int"""
        product_exist = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        if not product_exist:
            return "No existe un producto con esa ID para eliminar, verifica el campo y vuelve a intentarlo"
        self.db.delete(product_exist)
        self.db.commit()
        return "el producto fue eliminado correctamente"
