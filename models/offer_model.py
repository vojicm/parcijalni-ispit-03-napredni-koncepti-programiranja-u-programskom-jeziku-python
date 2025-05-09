from datetime import datetime, date
from typing import List



class OfferItem ():
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
        return f'{self.product_id}. {self.product_name}, {self.quantity}, '


class Offer ():
    def __init__(self,
                 offer_number:int, 
                 customer: str, 
                 offer_date: date, 
                 items:List[OfferItem],
                 sub_total:float,
                 tax: float, 
                 total: float):
        
        self.offer_number = offer_number
        self.customer = customer
        self.date = offer_date
        self.items = items
        self.sub_total = sub_total
        self.tax = tax
        self.total = total




    



