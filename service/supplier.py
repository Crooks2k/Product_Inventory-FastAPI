from models.supplier import Supplier as SupplierModel
from schemas.supplier import Supplier

class Supplier_Service():

    def __init__(self,db):
        self.db = db

    def get_supplier(self):
        """Use to get all supplier info (not require params)"""
        result = self.db.query(SupplierModel).all()
        return result

    def get_supplier_by_id(self,id:int):
        """Use to get one supplier info (need id: int with param)"""
        result = self.db.query(SupplierModel).filter(SupplierModel.id == id).first()
        return result    

    def add_supplier(self,supplier:Supplier):
        """Use to create suppliers (need supplier: supplier with params)"""

        existing_supplier = self.db.query(SupplierModel).filter(SupplierModel.id == supplier.id).first()
        if existing_supplier:
            return "Ya existe un proveedor con esa ID"

        new_supplier = SupplierModel(
            name=supplier.name,
            address=supplier.address,
            phone=supplier.phone,
            email=supplier.email
        )
        if new_supplier:
            self.db.add(new_supplier)
            self.db.commit()
            return "Proveedor agregado correctamente"
        
    def edit_supplier(self, data: Supplier):
        """Use to edit suppliers (need two params => id: int || supplier: supplier)"""
        supplier_exist: Supplier = self.db.query(SupplierModel).filter(SupplierModel.id == data.id).first()
        if not supplier_exist:
            return "No existe un proveedor con esa ID, verifica el campo y vuelve a intentarlo"
        
        supplier_exist.name = data.name
        supplier_exist.address = data.address
        supplier_exist.phone = data.phone
        supplier_exist.email = data.email
        self.db.commit()
        
        return "El proveedor fue editado correctamente"

    def delete_supplier(self, id: int):
        """Use to delete supplier, need one param => id: int"""
        supplier_exist = self.db.query(SupplierModel).filter(SupplierModel.id == id).first()
        if not supplier_exist:
            return "No existe un proveedor con esa ID para eliminar, verifica el campo y vuelve a intentarlo"
        self.db.delete(supplier_exist)
        self.db.commit()
        return "el proveedor fue eliminado correctamente"
