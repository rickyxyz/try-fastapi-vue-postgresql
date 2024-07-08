"""
models.py

Defines SQLAlchemy models for the application.

Dependencies:
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library.
- env: Imports database connection string.

Models:
- `Review`: Represents a review with `id`, `rating`, and `created_at` fields.

Functions:
- `get_reviews`: Class method to retrieve all reviews from the database session.
"""

from sqlalchemy import Column, Integer, DateTime, create_engine, func
from sqlalchemy.orm import sessionmaker, declarative_base
from app.env import DB_CONNECTION_STRING

# Database engine and session setup
engine = create_engine(DB_CONNECTION_STRING)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy declarative base
Base = declarative_base()


# Review model class definition
class Review(Base):
    """
    SQLAlchemy model representing a review.

    Attributes:
    - `id`: Primary key integer ID.
    - `rating`: Integer field representing the rating of the review.
    - `created_at`: DateTime field representing the creation timestamp.
    """

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"id: {self.id}, rating: {self.rating}, created_at: {self.created_at}"

    @classmethod
    def get_reviews(cls, db):
        """
        Class method to retrieve all reviews from the database session.

        Parameters:
        - `db`: SQLAlchemy session object.

        Returns:
        - List of `Review` objects: All reviews stored in the database.
        """
        return db.query(cls).all()
