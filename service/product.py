from models.product import Product as ProductModel

class ProductService():

    def __init__(self,db):
        self.db = db

    def get_product(self):
        result = self.db.query(ProductModel).all()
        return result

    def get_product_by_id(self,id:int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result    


