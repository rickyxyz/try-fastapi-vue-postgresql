"""
env.py

Configuration file for environment variables.

Dependencies:
- os: Operating system interfaces.
- dotenv: Loads environment variables from .env files.
- configparser: Configuration file parser.

Environment Variables:
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_PORT`, `DB_HOST`: PostgreSQL database connection details.
- `DB_CONNECTION_STRING`: PostgreSQL connection string.
- `APP_PORT`, `APP_HOST`: FastAPI server configuration.
- `FRONTEND_URL`: URL of the frontend application for CORS.
"""

import os
from dotenv import load_dotenv
from configparser import ConfigParser

# Load environment variables from .env files
load_dotenv(dotenv_path="../.env")
load_dotenv(dotenv_path=".env")

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_HOST = os.getenv("POSTGRES_HOST")

# PostgreSQL database connection string
DB_CONNECTION_STRING = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# FastAPI server configuration
APP_PORT = os.getenv("APP_PORT")
APP_HOST = os.getenv("APP_HOST")

# Frontend URL for CORS configuration
FRONTEND_URL = os.getenv("FRONTEND_URL")
