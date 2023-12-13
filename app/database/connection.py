import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from sqlalchemy.engine import URL

load_dotenv()


class Database:
    _instance = None
    _engine = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            config = dict(
                drivername='postgresql+psycopg2',
                username=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("POSTGRES_HOST"),
                port=os.getenv("POSTGRES_PORT"),
                database=os.getenv("POSTGRES_DB"),
                query={"sslmode": "disable"}
            )
            database_url = URL(**config)
            if not database_url:
                raise ValueError("Database URL is not set in the environment variables.")
            cls._engine = create_engine(database_url)
            cls._session = sessionmaker(autocommit=False, autoflush=False, bind=cls._engine)
        return cls._instance

    def connect(self) -> Session:
        return self._session()

    def disconnect(self, session):
        session.close()


config = dict(
    drivername='postgresql+psycopg2',
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    database=os.getenv("POSTGRES_DB"),
    query={"sslmode": "disable"}
)
database_url = URL(**config)
engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
