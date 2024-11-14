# app_features/offers/repository_alchemy.py

from sqlalchemy import create_engine, Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import sessionmaker, relationship
from app_features.offers.model import Offer, OfferItem
from app_features.customers.repository_alchemy import CustomerModel
from utils.constants import DATABASE_PATH
from data.sqlalchemy_base import Base


class OfferModel(Base):
    __tablename__ = 'offers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    date = Column(String)
    sub_total = Column(Float)
    tax = Column(Float)
    total = Column(Float)

    # Define relationship to customer
    customer = relationship("CustomerModel", back_populates="offers")
    items = relationship("OfferItemModel", back_populates="offer", cascade="all, delete-orphan")


class OfferItemModel(Base):
    __tablename__ = 'offer_items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    offer_id = Column(Integer, ForeignKey('offers.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    item_total = Column(Float)

    # Relationships
    offer = relationship("OfferModel", back_populates="items")
    product = relationship("ProductModel")

    def calculate_item_total(self):
        """Calculate item total based on product price and quantity."""
        if self.product:
            self.item_total = self.product.price * self.quantity


class SQLAlchemyRepository:
    """
    SQLAlchemy repository for handling offer data storage and retrieval, with customer and item association.
    """

    def __init__(self, table_name):
        self.engine = create_engine(f"sqlite:///{DATABASE_PATH}")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_all(self):
        """Retrieve all offers with customer and items information from the table."""
        session = self.Session()
        offers = session.query(OfferModel).all()

        result = []
        for offer in offers:
            customer = CustomerModel(id=offer.customer.id, name=offer.customer.name, email=offer.customer.email,
                                     vat_id=offer.customer.vat_id)
            items = [OfferItem(product_id=item.product_id, product_name=item.product_name, description=item.description,
                               price=item.price, quantity=item.quantity) for item in offer.items]
            result.append(Offer(offer_number=offer.id, customer=customer, date=offer.date, items=items))

        session.close()
        return result

    def add(self, offer):
        """Add a new offer with associated customer and items."""
        session = self.Session()
        new_offer = OfferModel(
            customer_id=offer.customer.id,
            date=offer.date,
            sub_total=offer.sub_total,
            tax=offer.tax,
            total=offer.total
        )

        # Add items to the offer
        new_offer.items = [
            OfferItemModel(
                product_id=item.product_id,
                product_name=item.product_name,
                description=item.description,
                price=item.price,
                quantity=item.quantity,
                item_total=item.item_total
            )
            for item in offer.items
        ]

        session.add(new_offer)
        session.commit()
        session.close()

    def get_by_id(self, offer_id):
        """Retrieve an offer by ID with customer and items information."""
        session = self.Session()
        offer = session.query(OfferModel).filter_by(id=offer_id).first()

        if not offer:
            session.close()
            return None

        customer = CustomerModel(id=offer.customer.id, name=offer.customer.name, email=offer.customer.email,
                                 vat_id=offer.customer.vat_id)
        items = [OfferItem(product_id=item.product_id, product_name=item.product_name, description=item.description,
                           price=item.price, quantity=item.quantity) for item in offer.items]

        result = Offer(offer_number=offer.id, customer=customer, date=offer.date, items=items)
        session.close()
        return result
