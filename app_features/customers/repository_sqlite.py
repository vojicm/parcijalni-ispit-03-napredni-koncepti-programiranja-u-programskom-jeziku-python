# app_features/customers/repository_sqlite.py

import sqlite3
from app_features.customers.model import Customer
from utils.constants import DATABASE_PATH


class SQLiteRepository:
    """
    SQLite repository for handling customer data storage and retrieval.
    """

    def __init__(self, table_name):
        self.table_name = table_name
        self.connection = sqlite3.connect(f"{DATABASE_PATH}")
        self.cursor = self.connection.cursor()

    def get_all(self):
        """Retrieve all customers from the table."""
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        return [Customer(id=row[0], name=row[1], email=row[2], vat_id=row[3]) for row in rows]

    def add(self, customer):
        """Add a new customer to the table."""
        self.cursor.execute(f"INSERT INTO {self.table_name} (name, email, vat_id) VALUES (?, ?, ?)",
                            (customer.name, customer.email, customer.vat_id))
        self.connection.commit()

    def get_by_id(self, customer_id):
        """Retrieve a customer by ID."""
        self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE id = ?", (customer_id,))
        row = self.cursor.fetchone()
        return Customer(id=row[0], name=row[1], email=row[2], vat_id=row[3]) if row else None

    def __del__(self):
        """Close the database connection."""
        self.connection.close()
