from app_features.offers.ui import display_offers_menu
from app_features.products.ui import display_products_menu
from app_features.users.ui import display_users_menu


def main_menu(config):
    """
    Display the main menu for the application and handle user navigation.
    """
    while True:
        print("\n--- Main Menu ---")
        print("1. Manage Offers")
        print("2. Manage Products")
        print("3. Manage Users")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            display_offers_menu(config)

        elif choice == "2":
            display_products_menu(config)

        elif choice == "3":
            display_users_menu(config)

        elif choice == "4":
            print("Exiting application.")
            break

        else:
            print("Invalid option, please try again.")
