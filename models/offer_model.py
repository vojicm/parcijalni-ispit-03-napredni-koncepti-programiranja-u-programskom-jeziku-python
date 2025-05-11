from datetime import datetime as dt
from typing import List, Tuple

from database import commit_in_db, create_offer_query

from .customer_model import Customer
from .product_model import Product, ProductItem



class Offer:
    def __init__(self,
                 offer_number:int, 
                 date_str: str = dt.today().strftime('%Y-%m-%d'),
                 customer: int = 0, 
                 items:List[ProductItem] = [],
                 tax: float = 25.0
                 ):
        
        self.offer_number = offer_number
        self.customer = customer
        self.date_str = date_str
        self.date = None
        self.items = items
        self.sub_total=0.00
        self.tax = tax
        self.tax_value = 0.0
        self.total = 0.00


        self.update_offer_date()
        self.update_totals()

    def update_offer_date (self):
        self.date = dt.strptime(self.date_str, '%Y-%m-%d')
    
    def update_totals(self): 
        if len(self.items)>0:
            for item in self.items:
               self.sub_total += item.item_total
        self.tax_value = self.sub_total * (self.tax/100)
        self.total = self.sub_total + self.tax_value
    
    def create_offer (self, offer: Tuple):
        commit_in_db(create_offer_query, offer)


    def get_offer (self):
        pass

    def update_offer (self):
        pass

    def delete_offer (self):
        pass

        
      





    



