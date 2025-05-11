import sqlite3
from typing import Tuple
from user_interface import load_data
from main import CUSTOMERS_FILE, PRODUCTS_FILE, OFFERS_FILE


def json_to_db (query:str, params: Tuple):
        
    with sqlite3.connect('db.sqlite3') as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()


    # INSERT CUSTOMER FROM JSON

def insert_customer_in_db(customer_tuple):
    create_customer_query = """INSERT INTO customers(name, email, vat_id) VALUES(?,?,?)"""
    json_to_db(create_customer_query, customer_tuple)

def populate_customer():
    customer_list = load_data (CUSTOMERS_FILE)
    for customer in customer_list:
        customer_tuple = (customer['name'], customer['email'], customer['vat_id'])
        insert_customer_in_db(customer_tuple)


    # INSERT PRODUCT FROM JSON

def insert_product_in_db (product_tuple):
    create_product_query = """INSERT INTO products(name, description, price) VALUES(?,?,?)"""
    json_to_db(create_product_query, product_tuple)

def populate_product():
    product_list = load_data (PRODUCTS_FILE)
    for product in product_list:
        product_tuple = (product['name'], product['description'], product ['price'])
        insert_product_in_db(product_tuple)


    # INSERT OFFER FROM JSON

def insert_offer_in_db (offer_tuple):
    create_product_query = """INSERT INTO offers(offer_number, date) VALUES(?,?)"""
    json_to_db(create_product_query, offer_tuple)

def populate_offer():
    offer_list = load_data (OFFERS_FILE)
    for offer in offer_list:
        offer_tuple = (offer['offer_number'], offer['date'])
        insert_offer_in_db(offer_tuple)


    # INSERT PRODUCT_ITEM FROM JSON

def insert_product_item_in_db (product_item_tuple):
    create_product_item_query = """INSERT INTO product_items(name, description, quantity, offer_id, product_id) VALUES(?,?,?,?,?)"""
    json_to_db(create_product_item_query, product_item_tuple)

def populate_product_item():
    offer_list = load_data (OFFERS_FILE)
    for offer in offer_list:
        offer_id = offer['offer_number']
        for item in offer['items']:
            product_item_tuple = (item['product_name'], item['description'], item['quantity'], offer_id, item['product_id'])
            insert_product_item_in_db(product_item_tuple)
