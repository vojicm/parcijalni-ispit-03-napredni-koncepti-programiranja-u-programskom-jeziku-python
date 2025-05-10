import sqlite3


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
    date TEXT NOT NULL
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


# CREATE
    # CREATE CUSTOMER
create_customer = """INSERT INTO customers(name, email, vat_id) VALUES(?,?,?)"""
    # CREATE OFFER
create_offer = """INSERT INTO offers(offer_number, date) VALUES(?,?)"""
    # CREATE PRODUCT
create_product = """INSERT INTO products(name, description, price) VALUES(?,?,?)"""
    # CREATE PRODUCT_ITEM
create_product_item = """INSERT INTO product_items(name, description, quantity, offer_id, product_id) VALUES(?,?,?,?,?)"""

# GET
    # GET CUSTOMER
get_customer = """SELECT * FROM customers WHERE id = ?"""
    # GET OFFER
get_offer = """SELECT * FROM offers WHERE id = ?"""
    # GET PRODUCT
get_product = """SELECT * FROM products WHERE id = ?"""
    # GET PRODUCT_ITEM
get_product_item = """SELECT * FROM product_items WHERE id = ?"""

# GET_ALL
    # GET_ALL CUSTOMER
get_customer = """SELECT * FROM customers"""
    # GET_ALL OFFER
get_offer = """SELECT * FROM offers"""
    # GET_ALL PRODUCT
get_product = """SELECT * FROM products"""
    # GET_ALL PRODUCT_ITEM
get_product_item = """SELECT * FROM product_items"""

# UPDATE

    # UPDATE CUSTOMER
update_customer = """ UPDATE customers SET name = ?, email = ?, vat_id = ? WHERE id = ? """
    # UPDATE OFFER

    # UPDATE PRODUCT

    # UPDATE PRODUCT_ITEM

# DELETE

    # DELETE CUSTOMER

    # DELETE OFFER

    # DELETE PRODUCT

    # DELETE PRODUCT_ITEM



def create_db ():
    try:

        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute(create_customer_table) 
            cursor.execute(create_product_table) 
            cursor.execute(create_offer_table) 
            cursor.execute(create_product_item_table) 
            conn.commit()

    except Exception as ex:
        print (f'Dogodila se greska u create_tables: {ex}')


