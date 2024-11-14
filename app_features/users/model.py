# app_features/users/model.py

class User:
    """
    User data model representing a user in the system, structured according to JSONPlaceholder API.
    """

    def __init__(self, id=None, name="", username="", email="", street="", suite="", city="", zipcode="", phone="", website="", company_name=""):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.phone = phone
        self.website = website
        self.company_name = company_name

    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', username='{self.username}', email='{self.email}', "
                f"address='{self.street}, {self.suite}, {self.city}, {self.zipcode}', phone='{self.phone}', "
                f"website='{self.website}', company_name='{self.company_name}')")
