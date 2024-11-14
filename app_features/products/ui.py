# app_features/products/ui.py

from app_features.products.service import ProductService


def display_products_menu(config):
    """
    Display menu for managing products and handle user input.
    """
    service = ProductService(config)

    while True:
        print("\n--- Product Management ---")
        print("1. View all products")
        print("2. Create a new product")
        print("3. View product by ID")
        print("4. Exit to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            products = service.get_all_products()
            for product in products:
                print(product)

        elif choice == "2":
            product_name = input("Enter product name: ")
            description = input("Enter product description: ")
            price = float(input("Enter product price: "))
            service.create_product(product_name, description, price)
            print("Product created successfully.")

        elif choice == "3":
            product_id = int(input("Enter product ID: "))
            product = service.get_product_by_id(product_id)
            if product:
                print(product)
            else:
                print("Product not found.")

        elif choice == "4":
            break

        else:
            print("Invalid option, please try again.")
