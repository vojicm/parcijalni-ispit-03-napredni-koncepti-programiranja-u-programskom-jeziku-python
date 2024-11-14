from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from app_features.products.model import Product
from utils.constants import DATABASE_PATH
from data.sqlalchemy_base import Base


class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)

class SQLAlchemyRepository:
    """
    SQLAlchemy repository for handling product data storage and retrieval.
    """

    def __init__(self, table_name):
        self.engine = create_engine(f"sqlite:///{DATABASE_PATH}")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_all(self):
        """Retrieve all products from the table."""
        session = self.Session()
        products = session.query(ProductModel).all()
        result = [Product(id=product.id, name=product.name, description=product.description, price=product.price) for product in products]
        session.close()
        return result

    def add(self, product):
        """Add a new product to the table."""
        session = self.Session()
        new_product = ProductModel(name=product.name, description=product.description, price=product.price)
        session.add(new_product)
        session.commit()
        session.close()

    def get_by_id(self, product_id):
        """Retrieve a product by ID."""
        session = self.Session()
        product = session.query(ProductModel).filter_by(id=product_id).first()
        session.close()
        return Product(id=product.id, name=product.name, description=product.description, price=product.price) if product else None
