# app_features/offers/service.py

from app_features.offers.model import Offer, OfferItem
from data.sqlite_repository import SQLiteRepository
from data.sqlalchemy_repository import SQLAlchemyRepository
from utils.date_utils import current_date_str


class OfferService:
    """
    Service layer for handling business logic related to offers.
    """

    def __init__(self, config):
        # Choose repository based on config
        if config.database_type == "sqlite3":
            self.repository = SQLiteRepository("offers")
        else:
            self.repository = SQLAlchemyRepository("offers")

    def get_all_offers(self):
        """Retrieve all offers."""
        return self.repository.get_all()

    def create_offer(self, customer, items):
        """Create a new offer associated with a customer."""
        offer = Offer(customer=customer, items=items, date=current_date_str())
        self.repository.add(offer)

    def get_offer_by_id(self, offer_id):
        """Retrieve an offer by its ID."""
        return self.repository.get_by_id(offer_id)
