import sqlite3
from typing import Tuple

from database import commit_in_db, create_product_query


class Product:
    def __init__(self, 
                 id: int, 
                 name: str, 
                 description: str, 
                 price: float):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
    
    def create_product (self, product: Tuple):
        commit_in_db(create_product_query, product)

    def get_product (self):
        pass

    def update_product (self):
        pass

    def delete_product (self):
        pass

class ProductItem:
    def __init__(self, 
                 product: Product = None,
                 quantity: float = 1, 
                 ):
        self.product = product
        self.quantity = quantity
        self.item_total = 0.00
        
        self.calculate_item_total()

    def calculate_item_total (self):
        if self.product != None:
            self.item_total = self.product.price * self.quantity

    
    def create_productItem (self):
        pass

    def get_productItem (self):
        pass

    def update_productItem (self):
        pass

    def delete_productItem (self):
        pass
