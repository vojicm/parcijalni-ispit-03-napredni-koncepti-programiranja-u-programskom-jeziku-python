# app_features/products/model.py

class Product:
    """
    Product data model representing a product in the system.
    """

    def __init__(self, id=None, name="", description="", price=0.0):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return (f"Product(id={self.id}, name='{self.name}', "
                f"description='{self.description}', price={self.price})")
