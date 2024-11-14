# app_features/offers/ui.py

from app_features.offers.service import OfferService
from app_features.customers.service import CustomerService


def display_offers_menu(config):
    """
    Display menu for managing offers and handle user input.
    """
    offer_service = OfferService(config)
    customer_service = CustomerService(config)

    while True:
        print("\n--- Offer Management ---")
        print("1. View all offers")
        print("2. Create a new offer")
        print("3. View offer by ID")
        print("4. Exit to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            offers = offer_service.get_all_offers()
            for offer in offers:
                print(offer)

        elif choice == "2":
            customer_id = int(input("Enter customer ID for this offer: "))
            customer = customer_service.get_customer_by_id(customer_id)
            if not customer:
                print("Customer not found.")
                continue

            items = []  # Placeholder for creating OfferItems
            while True:
                product_id = int(input("Enter product ID (or 0 to finish): "))
                if product_id == 0:
                    break
                product_name = input("Enter product name: ")
                description = input("Enter product description: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter quantity: "))
                item = OfferItem(product_id, product_name, description, price, quantity)
                items.append(item)

            offer_service.create_offer(customer, items)
            print("Offer created successfully.")

        elif choice == "3":
            offer_id = int(input("Enter offer ID: "))
            offer = offer_service.get_offer_by_id(offer_id)
            if offer:
                print(offer)
            else:
                print("Offer not found.")

        elif choice == "4":
            break

        else:
            print("Invalid option, please try again.")
