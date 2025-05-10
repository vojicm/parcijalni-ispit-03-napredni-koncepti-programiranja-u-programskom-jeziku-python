
from datetime import datetime
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

    while True:
        menu(offers, products, customers)
        


if __name__ == "__main__":
    create_db()
    user_service = UserService(user_id=5)
    print(user_service.user.name)
    main()
