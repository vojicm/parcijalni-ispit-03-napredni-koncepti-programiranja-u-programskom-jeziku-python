# database_setup.py
import random
from datetime import datetime
from sqlalchemy import create_engine
import sqlite3

from sqlalchemy.orm import sessionmaker

from app_features.customers.repository_alchemy import CustomerModel
from app_features.offers.repository_alchemy import OfferItemModel, OfferModel
from app_features.products.repository_alchemy import ProductModel
from utils.constants import DATABASE_PATH
from data.sqlalchemy_base import Base


# Sample data
product_names = [
    "Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch", "Camera", "Keyboard",
    "Mouse", "Monitor", "Printer", "Router", "USB Drive", "External Hard Drive", "Charger", "Speaker"
]

customer_names = [
    "John Doe", "Jane Smith", "Alice Johnson", "Michael Brown", "Linda Williams",
    "James Jones", "Barbara Garcia", "Robert Miller", "Patricia Wilson", "David Moore"
]


def setup_database_alchemy():
    """
    Set up the database and create tables using SQLAlchemy models.
    """
    engine = create_engine(f"sqlite:///{DATABASE_PATH}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    seed_products(session)
    seed_customers(session)
    seed_offers(session)

def setup_database_sqlite():
    """
    Set up the database and create tables using sqlite3 module.
    """
    connection = sqlite3.connect(f'{DATABASE_PATH}')
    cursor = connection.cursor()

    # Create customers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            vat_id TEXT
        )
    """)

    # Create offers table (linked to customers)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS offers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            offer_number INTEGER,
            customer_id INTEGER,
            date TEXT,
            sub_total REAL,
            tax REAL,
            total REAL,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )
    """)

    # Create offer_items table (linked to offers)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS offer_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            offer_id INTEGER,
            product_id INTEGER,
            product_name TEXT,
            description TEXT,
            price REAL,
            quantity INTEGER,
            item_total REAL,
            FOREIGN KEY (offer_id) REFERENCES offers(id)
        )
    """)

    # Create products table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            price REAL
        )
    """)

    connection.commit()
    connection.close()
    print("Database tables created successfully with sqlite3.")


# Seed Products
def seed_products(session):
    for i, name in enumerate(product_names):
        price = round(random.uniform(10.0, 1000.0), 2)
        description = f"{name} with high quality features."
        product = ProductModel(name=name, description=description, price=price)
        session.add(product)
    session.commit()
    print("15 products have been seeded.")


# Seed Customers
def seed_customers(session):
    for name in customer_names:
        email = f"info@{name.replace(' ', '').lower()}.com"
        vat_id = f"{random.randint(10000000000, 99999999999)}"
        customer = CustomerModel(name=name, email=email, vat_id=vat_id)
        session.add(customer)
    session.commit()
    print("10 customers have been seeded.")


# Seed Offers
def seed_offers(session):
    customers = session.query(CustomerModel).all()
    products = session.query(ProductModel).all()

    for i in range(10):
        customer = random.choice(customers)
        date = datetime.now().strftime("%Y-%m-%d")
        num_items = random.randint(1, 6)
        offer_items = []
        sub_total = 0.0

        for _ in range(num_items):
            product = random.choice(products)
            quantity = random.randint(1, 5)
            item_total = product.price * quantity
            sub_total += item_total

            offer_item = OfferItemModel(
                product_id=product.id,
                product_name=product.name,
                description=product.description,
                price=product.price,
                quantity=quantity,
                item_total=item_total
            )
            offer_items.append(offer_item)

        tax = round(sub_total * 0.1, 2)  # Assuming a 10% tax rate
        total = sub_total + tax

        offer = OfferModel(
            customer_id=customer.id,
            date=date,
            sub_total=sub_total,
            tax=tax,
            total=total,
            items=offer_items
        )

        session.add(offer)
    session.commit()
    print("10 offers with offer items have been seeded.")