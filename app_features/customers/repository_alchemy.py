# app_features/customers/repository_alchemy.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from utils.constants import DATABASE_PATH
from data.sqlalchemy_base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app_features.customers.model import Customer


class CustomerModel(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    vat_id = Column(String)

    # Define relationship to offers
    offers = relationship("OfferModel", back_populates="customer")


class SQLAlchemyRepository:
    """
    SQLAlchemy repository for handling customer data storage and retrieval.
    """

    def __init__(self, table_name):
        self.engine = create_engine(f"sqlite:///{DATABASE_PATH}")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_all(self):
        """Retrieve all customers from the table."""
        session = self.Session()
        customers = session.query(CustomerModel).all()
        result = [Customer(id=customer.id, name=customer.name, email=customer.email, vat_id=customer.vat_id) for
                  customer in customers]
        session.close()
        return result

    def add(self, customer):
        """Add a new customer to the table."""
        session = self.Session()
        new_customer = CustomerModel(name=customer.name, email=customer.email, vat_id=customer.vat_id)
        session.add(new_customer)
        session.commit()
        session.close()

    def get_by_id(self, customer_id):
        """Retrieve a customer by ID."""
        session = self.Session()
        customer = session.query(CustomerModel).filter_by(id=customer_id).first()
        session.close()
        return Customer(id=customer.id, name=customer.name, email=customer.email,
                        vat_id=customer.vat_id) if customer else None
