# app_features/products/repository_sqlite.py

import sqlite3
from app_features.products.model import Product
from utils.constants import DATABASE_PATH


class SQLiteRepository:
    """
    SQLite repository for handling product data storage and retrieval.
    """

    def __init__(self, table_name):
        self.table_name = table_name
        self.connection = sqlite3.connect(f"{DATABASE_PATH}")
        self.cursor = self.connection.cursor()

    def get_all(self):
        """Retrieve all products from the table."""
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        return [Product(id=row[0], name=row[1], description=row[2], price=row[3]) for row in rows]

    def add(self, product):
        """Add a new product to the table."""
        self.cursor.execute(f"INSERT INTO {self.table_name} (name, description, price) VALUES (?, ?, ?)",
                            (product.name, product.description, product.price))
        self.connection.commit()

    def get_by_id(self, product_id):
        """Retrieve a product by ID."""
        self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE id = ?", (product_id,))
        row = self.cursor.fetchone()
        return Product(id=row[0], name=row[1], description=row[2], price=row[3]) if row else None

    def __del__(self):
        """Close the database connection."""
        self.connection.close()
