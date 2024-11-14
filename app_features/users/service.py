# app_features/users/service.py

from app_features.users.model import User
from app_features.users.repository import UserRepository


class UserService:
    """
    Service layer for handling business logic related to users.
    """

    def __init__(self, config):
        self.repository = UserRepository(config.user_api_url)

    def get_all_users(self):
        """Retrieve all users."""
        return self.repository.get_all()

    def get_user_by_id(self, user_id):
        """Retrieve a user by their ID."""
        return self.repository.get_by_id(user_id)
