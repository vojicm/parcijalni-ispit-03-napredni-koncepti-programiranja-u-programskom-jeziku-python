import sqlite3




class Customer :
    def __init__(self, 
                 name: str, 
                 email: str, 
                 vat_id: str):
        self.name = name
        self.email = email
        self.vat_id = vat_id
    
    def create_customer (self):
        pass

    def get_customer (self):
        pass

    def update_customer (self):
        pass

    def delete_customer (self):
        pass
