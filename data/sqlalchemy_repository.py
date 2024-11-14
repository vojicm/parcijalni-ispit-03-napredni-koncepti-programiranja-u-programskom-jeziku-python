# data/sqlalchemy_repository.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.constants import DATABASE_PATH
from data.sqlalchemy_base import Base


class SQLAlchemyRepository:
    """
    Base SQLAlchemy repository for handling data storage and retrieval.
    This can be extended by specific repositories for different app_features.
    """

    def __init__(self):
        self.engine = create_engine(f"sqlite:///{DATABASE_PATH}")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_all(self, model):
        """Retrieve all records of a specified model from the database."""
        session = self.Session()
        records = session.query(model).all()
        session.close()
        return records

    def get_by_id(self, model, record_id):
        """Retrieve a record by ID of a specified model from the database."""
        session = self.Session()
        record = session.query(model).get(record_id)
        session.close()
        return record

    def add(self, instance):
        """Add a new record (instance) to the database."""
        session = self.Session()
        session.add(instance)
        session.commit()
        session.close()
