# app_features/customers/service.py

from app_features.customers.model import Customer
from data.sqlite_repository import SQLiteRepository
from data.sqlalchemy_repository import SQLAlchemyRepository


class CustomerService:
    """
    Service layer for handling business logic related to customers.
    """

    def __init__(self, config):
        # Choose repository based on config
        if config.database_type == "sqlite3":
            self.repository = SQLiteRepository("customers")
        else:
            self.repository = SQLAlchemyRepository("customers")

    def get_all_customers(self):
        """Retrieve all customers."""
        return self.repository.get_all()

    def create_customer(self, name, email, vat_id):
        """Create a new customer."""
        customer = Customer(name=name, email=email, vat_id=vat_id)
        self.repository.add(customer)

    def get_customer_by_id(self, customer_id):
        """Retrieve a customer by their ID."""
        return self.repository.get_by_id(customer_id)
