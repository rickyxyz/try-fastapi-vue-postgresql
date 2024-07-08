"""
schemas.py

Defines Pydantic models for request and response schemas.

Dependencies:
- pydantic: Data validation and settings management using Python type annotations.

Models:
- `ReviewBase`: Base Pydantic model for review with `rating` field.
- `ReviewResponse`: Pydantic model representing a review response with `id`, `rating`, and `created_at` fields.
- `ReviewCreate`: Pydantic model for creating a review with `rating` field.

Configuration:
- `orm_mode`: Enables SQLAlchemy ORM mode for `ReviewResponse`.
"""

from pydantic import BaseModel, Field
from datetime import datetime


# Base Pydantic model for review with rating field
class ReviewBase(BaseModel):
    rating: int


# Pydantic model representing a review response with id, rating, and created_at fields
class ReviewResponse(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Pydantic model for creating a review with rating field
class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
