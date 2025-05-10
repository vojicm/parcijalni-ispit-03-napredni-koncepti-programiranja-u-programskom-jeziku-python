import sqlite3





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
    
    def __repr__(self):
        return f'{self.name} ({self.id}) - {self.price}'
    
    def create_product (self):
        pass

    def get_product (self):
        pass

    def update_product (self):
        pass

    def delete_product (self):
        pass
