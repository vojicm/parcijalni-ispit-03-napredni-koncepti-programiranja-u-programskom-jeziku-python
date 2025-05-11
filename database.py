import sqlite3
from typing import Any, Tuple



# SQL Queries
create_customer_table = """
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    vat_id TEXT NOT NULL
);
"""

create_product_table = """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NULL,
    price FLOAT NOT NULL
);
"""

create_offer_table = """
CREATE TABLE IF NOT EXISTS offers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    offer_number INTEGER NOT NULL,
    date TEXT NOT NULL,
    customer_id INTEGER,
    sub_total FLOAT,
    tax FLOAT,
    total FLOAT,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);
"""

create_product_item_table = """
CREATE TABLE IF NOT EXISTS product_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NULL,
    quantity FLOAT NOT NULL,
    offer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (offer_id) REFERENCES offers (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
);
"""
def create_db ():
    try:

        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute(create_customer_table) 
            cursor.execute(create_product_table) 
            cursor.execute(create_offer_table) 
            cursor.execute(create_product_item_table) 
            conn.commit()


            cursor.execute('SELECT COUNT(*) FROM customers')
            customer_count = cursor.fetchone()[0]

        if customer_count == 0:
            from models.from_json_to_db import populate_customer, populate_product, populate_offer, populate_product_item
            populate_customer()
            populate_product()
            populate_offer()
            populate_product_item()

    except Exception as ex:
        print (f'Dogodila se greska u create_tables: {ex}')



def commit_in_db(query:str, params: Any = ()):
    try:
        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute(query, params) 
            conn.commit()
    except Exception as ex:
        print (f'Dogodila se greska u create_in_db: {ex}')

def fetchall_from_db(query:str, params: Any = ()):
    try:
        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute(query, params) 
            return cursor.fetchall()
    except Exception as ex:
        print (f'Dogodila se greska u fetchall_from_db: {ex}')


# CREATE
    # CREATE CUSTOMER
create_customer_query = """INSERT INTO customers(name, email, vat_id) VALUES(?,?,?)"""
def create_customer(customer: Tuple):
    commit_in_db(create_customer_query, customer)
    # CREATE OFFER
create_offer_query= """INSERT INTO offers(offer_number, date, customer_id, sub_total, tax, total) VALUES (?, ?, ?, ?, ?, ?)"""

    # CREATE PRODUCT
create_product_query = """INSERT INTO products(name, description, price) VALUES(?,?,?)"""
    # CREATE PRODUCT_ITEM
create_product_item_query = """INSERT INTO product_items(name, description, quantity, offer_id, product_id) VALUES(?,?,?,?,?)"""
def create_product_item(product_item:Tuple):
    commit_in_db(create_product_item_query, product_item)
# GET
    # GET CUSTOMER
get_customer_query = """SELECT * FROM customers WHERE id = ?"""
def get_customer(customer_id:Tuple):
    fetchall_from_db(get_customer_query, customer_id)
    # GET OFFER
get_offer_query = """SELECT * FROM offers WHERE id = ?"""
def get_offer(offer_id:Tuple):
    fetchall_from_db(get_offer_query, offer_id)   #(1,) - offers id=1
    # GET PRODUCT
get_product_query = """SELECT * FROM products WHERE id = ?"""
def get_product(product_id:Tuple):
    fetchall_from_db(get_product_query, product_id) 
    # GET PRODUCT_ITEM
get_product_item_query = """SELECT * FROM product_items WHERE id = ?"""
def get_product_item(product_item_id:Tuple):
    fetchall_from_db(get_product_item_query, product_item_id) 

# GET_ALL
    # GET_ALL CUSTOMER
get_customers_query = """SELECT * FROM customers"""
def get_customers():
    fetchall_from_db(get_customers_query)
    # GET_ALL OFFER
get_offers_query = """SELECT * FROM offers"""
def get_offers():
    fetchall_from_db(get_offers_query)
    # GET_ALL PRODUCT
get_products_query = """SELECT * FROM products"""
def get_products():
    fetchall_from_db(get_products_query)
    # GET_ALL PRODUCT_ITEM
get_product_items_query = """SELECT * FROM product_items"""
def get_product_items():
    fetchall_from_db(get_product_items_query)

# UPDATE

    # UPDATE CUSTOMER
update_customer_query = """ UPDATE customers SET name = ?, email = ?, vat_id = ? WHERE id = ? """
def update_customer(customer: Tuple):
    commit_in_db(update_customer_query, customer)
    # UPDATE OFFER
update_offer_query = """ UPDATE offers SET offer_number = ?, date = ? WHERE id = ? """
def update_offer(offer: Tuple):
    commit_in_db(update_offer_query, offer)
    # UPDATE PRODUCT
update_product_query = """ UPDATE products SET name = ?, description = ?, price = ? WHERE id = ? """
def update_product(product: Tuple):
    commit_in_db(update_product_query, product)
    # UPDATE PRODUCT_ITEM
update_product_item_query = """ UPDATE product_items SET name=?, description=?, quantity=?, offer_id=?, product_id=? WHERE id = ? """
def update_product_item(product_item: Tuple):
    commit_in_db(update_product_item_query, product_item)
    
# DELETE

    # DELETE CUSTOMER
delete_customer_query = """DELETE FROM customers WHERE id = ?"""
def delete_customer(customer_id:Tuple):
    commit_in_db(delete_customer_query, customer_id)
    # DELETE OFFER
delete_offer_query = """DELETE FROM offers WHERE id = ?"""
def delete_offer(offer_id:Tuple):
    commit_in_db(delete_offer_query, offer_id)
    # DELETE PRODUCT
delete_product_query = """DELETE FROM products WHERE id = ?"""
def delete_product(product_id:Tuple):
    commit_in_db(delete_product_query, product_id)
    # DELETE PRODUCT_ITEM
delete_product_item_query = """DELETE FROM product_items WHERE id = ?"""
def delete_product_item(product_item_id:Tuple):
    commit_in_db(delete_product_item_query, product_item_id)

