"""
main.py

This file contains the main application setup using FastAPI for managing reviews.

Dependencies:
- FastAPI: Web framework for building APIs with Python.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library.
- CORS Middleware: FastAPI middleware for Cross-Origin Resource Sharing.
- Logging: Python module for error logging.

Modules:
- `logging`: Configures error logging to a file (`error.log`).
- `get_db`: Dependency function to provide a database session to endpoint functions.
- Exception Handlers: Handles HTTP exceptions and logs errors.
- `/reviews/` Endpoints:
  - `POST`: Creates a new review with a specified rating.
  - `GET`: Retrieves all reviews stored in the database.

Execution:
- Runs the FastAPI application using uvicorn server.

Environment Variables:
- `APP_HOST`, `APP_PORT`: Host and port configuration for the FastAPI server.
- `FRONTEND_URL`: URL of the frontend application for CORS configuration.
"""

import logging
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.models import Base, Review, engine, SessionLocal
from app.schemas import ReviewCreate, ReviewResponse
from fastapi.middleware.cors import CORSMiddleware
from app.env import APP_HOST, APP_PORT, FRONTEND_URL

# Create all database tables based on models
Base.metadata.create_all(bind=engine)

# FastAPI application instance
app = FastAPI()

# Configure CORS middleware to allow requests from specified frontend URL
origins = [FRONTEND_URL]
print(origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Configure logging to a file
logging.basicConfig(
    filename="logs/error.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# Dependency function to provide a database session to endpoint functions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Exception handler for HTTP exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


# Endpoint to create a new review
@app.post("/reviews/", response_model=ReviewResponse)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new review with a specified rating.

    Parameters:
    - `review`: Pydantic model `ReviewCreate` containing the rating.

    Returns:
    - `ReviewResponse`: Pydantic model representing the created review.
    """
    try:
        db_review = Review(rating=review.rating)
        db.add(db_review)
        db.commit()
        db.refresh(db_review)
        return db_review
    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
        raise HTTPException(status_code=400, detail=f"Invalid input: {ve}")
    except Exception as e:
        logging.error(f"Internal Server Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Endpoint to retrieve all reviews
@app.get("/reviews/", response_model=list[ReviewResponse])
def read_reviews(db: Session = Depends(get_db)):
    """
    Endpoint to retrieve all reviews stored in the database.

    Returns:
    - List of `ReviewResponse`: Pydantic model representing all reviews.
    """
    try:
        return db.query(Review).all()
    except Exception as e:
        logging.error(f"Internal Server Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Run the application if executed directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=APP_HOST, port=int(APP_PORT), debug=True)
