from datetime import datetime as dt
from typing import List

from .product_model import Product

from .customer_model import Customer



class OfferItem:
    def __init__(self, 
                 product_id:int,
                 product_name: str,
                 description:str,
                 quantity:int,
                 item_total: float):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.quantity = quantity
        self.item_total = item_total
    
    def __repr__(self):
        return f'{self.product_id}. {self.product_name}, {self.quantity}'



class Offer:
    def __init__(self,
                 offer_number:int, 
                 customer: Customer = None, 
                 offer_date: str = dt.today().strftime('%Y-%m-%d'), 
                 items:List[Product] = [],
                 sub_total: float,
                 tax: float, 
                 total: float):
        
        self.offer_number = offer_number
        self.customer = customer
        self.date = offer_date
        self.items = items
        self.sub_total = sub_total
        self.tax = tax
        self.total = total

    def __repr__(self):
        return f'{self.offer_number}. {self.customer}, {self.total}, '




    



