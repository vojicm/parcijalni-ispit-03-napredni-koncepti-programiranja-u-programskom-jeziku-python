# app_features/products/service.py

from app_features.products.model import Product
from data.sqlite_repository import SQLiteRepository
from data.sqlalchemy_repository import SQLAlchemyRepository


class ProductService:
    """
    Service layer for handling business logic related to products.
    """

    def __init__(self, config):
        # Choose repository based on config
        if config.database_type == "sqlite3":
            self.repository = SQLiteRepository("products")
        else:
            self.repository = SQLAlchemyRepository("products")

    def get_all_products(self):
        """Retrieve all products."""
        return self.repository.get_all()

    def create_product(self, name, description, price):
        """Create a new product."""
        product = Product(name=name, description=description, price=price)
        self.repository.add(product)

    def get_product_by_id(self, product_id):
        """Retrieve a product by its ID."""
        return self.repository.get_by_id(product_id)
