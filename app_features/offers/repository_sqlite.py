# app_features/offers/repository_sqlite.py

import sqlite3
from app_features.offers.model import Offer, OfferItem
from app_features.customers.model import Customer
from utils.constants import DATABASE_PATH


class SQLiteRepository:
    """
    SQLite repository for handling offer data storage and retrieval, with customer and items association.
    """

    def __init__(self, table_name):
        self.table_name = table_name
        self.connection = sqlite3.connect(f"{DATABASE_PATH}")
        self.cursor = self.connection.cursor()

    def get_all(self):
        """Retrieve all offers with customer and items information."""
        self.cursor.execute(f"""
            SELECT offers.id, offers.date, offers.sub_total, offers.tax, offers.total,
                   customers.id, customers.name, customers.email, customers.vat_id
            FROM {self.table_name}
            JOIN customers ON offers.customer_id = customers.id
        """)
        rows = self.cursor.fetchall()

        offers = []
        for row in rows:
            customer = Customer(id=row[5], name=row[6], email=row[7], vat_id=row[8])
            offer = Offer(id=row[0], date=row[1], sub_total=row[2], tax=row[3], total=row[4], customer=customer)

            # Retrieve offer items for each offer
            self.cursor.execute(
                "SELECT product_id, product_name, description, price, quantity, item_total FROM offer_items WHERE offer_id = ?",
                (offer.id,))
            items = [OfferItem(*item_row) for item_row in self.cursor.fetchall()]
            offer.items = items
            offers.append(offer)

        return offers

    def add(self, offer):
        """Add a new offer to the table with associated customer and items."""
        self.cursor.execute(
            f"INSERT INTO {self.table_name} (customer_id, date, sub_total, tax, total) VALUES (?, ?, ?, ?, ?)",
            (offer.customer.id, offer.date, offer.sub_total, offer.tax, offer.total))
        offer_id = self.cursor.lastrowid

        for item in offer.items:
            self.cursor.execute(
                "INSERT INTO offer_items (offer_id, product_id, product_name, description, price, quantity, item_total) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (offer_id, item.product_id, item.product_name, item.description, item.price, item.quantity,
                 item.item_total))

        self.connection.commit()

    def get_by_id(self, offer_id):
        """Retrieve an offer by ID with customer and items information."""
        self.cursor.execute(f"""
            SELECT offers.id, offers.date, offers.sub_total, offers.tax, offers.total,
                   customers.id, customers.name, customers.email, customers.vat_id
            FROM {self.table_name}
            JOIN customers ON offers.customer_id = customers.id
            WHERE offers.id = ?
        """, (offer_id,))
        row = self.cursor.fetchone()

        if not row:
            return None

        customer = Customer(id=row[5], name=row[6], email=row[7], vat_id=row[8])
        offer = Offer(id=row[0], date=row[1], sub_total=row[2], tax=row[3], total=row[4], customer=customer)

        # Retrieve offer items for this offer
        self.cursor.execute(
            "SELECT product_id, product_name, description, price, quantity, item_total FROM offer_items WHERE offer_id = ?",
            (offer.id,))
        items = [OfferItem(*item_row) for item_row in self.cursor.fetchall()]
        offer.items = items

        return offer

    def __del__(self):
        """Close the database connection."""
        self.connection.close()
