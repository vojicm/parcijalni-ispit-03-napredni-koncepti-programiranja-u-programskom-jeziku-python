
from datetime import datetime
import sys
from database import create_db
from services import UserService

from user_interface import (load_data, menu, print_offer)


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def main():
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)
    
    
    user_log = int(input('Unesite vas ID: '))
    userservice = UserService(user_id=user_log)

    if userservice.user != None:
        print (userservice.user.name)
        while True:
            menu(offers, products, customers)
            
    else:
        print("User not found.")


if __name__ == "__main__":
    create_db()
   
    main()
