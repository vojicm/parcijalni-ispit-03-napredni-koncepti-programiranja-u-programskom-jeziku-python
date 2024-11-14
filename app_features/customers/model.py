# app_features/customers/model.py

class Customer:
    """
    Customer data model representing a customer in the system.
    """

    def __init__(self, id=None, name="", email="", vat_id=""):
        self.id = id
        self.name = name
        self.email = email
        self.vat_id = vat_id

    def __repr__(self):
        return (f"Customer(id={self.id}, name='{self.name}', email='{self.email}', "
                f"vat_id='{self.vat_id}')")
