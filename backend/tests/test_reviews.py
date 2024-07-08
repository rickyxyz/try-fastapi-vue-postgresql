import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.models import Base
import os
from dotenv import load_dotenv

# Load environment variables from .env files
load_dotenv(dotenv_path="../../.env")
load_dotenv(dotenv_path="../.env")


# PostgreSQL connection details from environment variables
DB_NAME = os.getenv("POSTGRES_TEST_DB")
DB_USER = os.getenv("POSTGRES_TEST_USER")
DB_PASSWORD = os.getenv("POSTGRES_TEST_PASSWORD")
DB_PORT = os.getenv("POSTGRES_TEST_PORT")
DB_HOST = os.getenv("POSTGRES_TEST_HOST")


# SQLAlchemy database URL for local PostgreSQL
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# SQLAlchemy engine and session setup for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


# Fixture for overriding get_db dependency with a testing session
@pytest.fixture(scope="module")
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# Fixture for creating a TestClient instance for API testing
@pytest.fixture
def test_client():
    return TestClient(app)


# Test cases for creating reviews with different scenarios
def test_create_review_valid(test_client, override_get_db):
    review_data = {"rating": 4}
    response = test_client.post("/reviews/", json=review_data)
    assert response.status_code == 200
    assert response.json()["rating"] == 4


def test_create_review_invalid_large(test_client, override_get_db):
    review_data = {"rating": 6}
    response = test_client.post("/reviews/", json=review_data)
    assert response.status_code == 422
    assert "detail" in response.json()


def test_create_review_invalid_small(test_client, override_get_db):
    review_data = {"rating": 0}
    response = test_client.post("/reviews/", json=review_data)
    assert response.status_code == 422
    assert "detail" in response.json()


# Test case for reading reviews
def test_read_reviews(test_client, override_get_db):
    response = test_client.get("/reviews/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
