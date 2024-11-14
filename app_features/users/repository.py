# app_features/users/repository.py

import requests
from app_features.users.model import User


class UserRepository:
    """
    Repository for handling user data retrieval from an external API.
    """

    def __init__(self, api_url):
        self.api_url = api_url

    def get_all(self):
        """Retrieve all users from the API."""
        response = requests.get(self.api_url)
        if response.status_code == 200:
            users_data = response.json()
            return [User(id=user["id"], name=user["name"], email=user["email"], address=user["address"]["city"])
                    for user in users_data]
        else:
            print("Error fetching users.")
            return []

    def get_by_id(self, user_id):
        """Retrieve a user by ID from the API."""
        response = requests.get(f"{self.api_url}/{user_id}")
        if response.status_code == 200:
            user_data = response.json()
            return User(id=user_data["id"], name=user_data["name"], email=user_data["email"],
                        address=user_data["address"]["city"])
        else:
            print("User not found.")
            return None
