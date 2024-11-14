# app_features/users/ui.py

from app_features.users.service import UserService


def display_users_menu(config):
    """
    Display menu for managing users and handle user input.
    """
    service = UserService(config)

    while True:
        print("\n--- User Management ---")
        print("1. View all users")
        print("2. View user by ID")
        print("3. Exit to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            users = service.get_all_users()
            for user in users:
                print(user)

        elif choice == "2":
            user_id = int(input("Enter user ID: "))
            user = service.get_user_by_id(user_id)
            if user:
                print(user)
            else:
                print("User not found.")

        elif choice == "3":
            break

        else:
            print("Invalid option, please try again.")
