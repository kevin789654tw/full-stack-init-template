import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine

env_path = Path(__file__).resolve().parents[2] / ".env"  # ./backend/
load_dotenv(dotenv_path=env_path, override=False)


class Database:
    """Database manager class to handle engine, sessions, and table creation."""

    _engine: Engine | None = None

    @staticmethod
    def get_database_url() -> str:
        """
        Retrieve the database connection URL from environment variables.

        Returns:
            str: The database connection string.

        Raises:
            ValueError: If `DATABASE_URL` is not set in the environment.
        """
        url = os.getenv("DATABASE_URL")
        if not url:
            raise ValueError("DATABASE_URL not set")
        return url

    @classmethod
    def get_engine(cls) -> Engine:
        """
        Get a SQLAlchemy engine instance.

        Returns:
            Engine: A SQLAlchemy engine connected to the configured database.
        """
        if cls._engine is None:
            cls._engine = create_engine(cls.get_database_url(), echo=True)
        return cls._engine

    @classmethod
    def create_db_and_tables(cls, custom_engine: Engine | None = None) -> None:
        """
        Create all database tables defined in SQLModel metadata.

        Args:
            custom_engine (Engine | None, optional):
                A custom SQLAlchemy engine to use.
                If not provided, the default engine from get_engine() is used.

        Returns:
            None
        """
        SQLModel.metadata.create_all(custom_engine or cls.get_engine())

    @classmethod
    def session(cls) -> Session:
        """
        Create and return a new database session using the configured engine.

        Returns:
            Session: A SQLModel session object connected to the database engine.
        """
        return Session(cls.get_engine())
