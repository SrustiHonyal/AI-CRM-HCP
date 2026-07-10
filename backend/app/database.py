from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus
import mysql.connector

from app.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME


# Encode special characters in password
encoded_password = quote_plus(DB_PASSWORD)


# SQLAlchemy Database URL
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{encoded_password}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=False
)


# SQLAlchemy session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for models
Base = declarative_base()


# FastAPI database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# MySQL connection for LangGraph tools
def get_connection():

    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )