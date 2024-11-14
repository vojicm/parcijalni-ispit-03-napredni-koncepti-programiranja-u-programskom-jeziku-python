# app_features/customers/ui.py

from app_features.customers.service import CustomerService


def display_customers_menu(config):
    """
    Display menu for managing customers and handle user input.
    """
    service = CustomerService(config)

    while True:
        print("\n--- Customer Management ---")
        print("1. View all customers")
        print("2. Create a new customer")
        print("3. View customer by ID")
        print("4. Exit to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            customers = service.get_all_customers()
            for customer in customers:
                print(customer)

        elif choice == "2":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            vat_id = input("Enter VAT ID: ")
            service.create_customer(name, email, vat_id)
            print("Customer created successfully.")

        elif choice == "3":
            customer_id = int(input("Enter customer ID: "))
            customer = service.get_customer_by_id(customer_id)
            if customer:
                print(customer)
            else:
                print("Customer not found.")

        elif choice == "4":
            break

        else:
            print("Invalid option, please try again.")
