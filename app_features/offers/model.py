# app_features/offers/model.py

from app_features.customers.model import Customer

class OfferItem:
    """
    Represents an item within an offer, including product details and totals.
    """
    def __init__(self, product_id: int, product_name: str, description: str,
                 price: float, quantity: int):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.item_total = price * quantity

    def __repr__(self):
        return (f"OfferItem(product_id={self.product_id}, product_name='{self.product_name}', "
                f"description='{self.description}', price={self.price}, quantity={self.quantity}, "
                f"item_total={self.item_total})")


class Offer:
    """
    Represents an offer with customer details, items, and calculated totals.
    """
    def __init__(self, offer_number: int, customer: Customer, date: str, items: list,
                 tax_rate: float = 0.1):
        self.offer_number = offer_number
        self.customer = customer  # Customer object
        self.date = date
        self.items = items
        self.sub_total = sum(item.item_total for item in items)
        self.tax = round(self.sub_total * tax_rate, 2)
        self.total = self.sub_total + self.tax

    def __repr__(self):
        return (f"Offer(offer_number={self.offer_number}, customer={self.customer}, "
                f"date='{self.date}', items={self.items}, sub_total={self.sub_total}, "
                f"tax={self.tax}, total={self.total})")
