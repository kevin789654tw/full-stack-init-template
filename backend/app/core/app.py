import os
from pathlib import Path

from app.api.item_routes import router as item_router
from app.db.database import Database
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class AppFactory:
    """Factory class to create and configure a FastAPI application instance."""

    def __init__(self, env_path: str | Path | None = None) -> None:
        # Load .env file
        if env_path is None:
            env_path = Path(__file__).resolve().parents[2] / ".env"  # ./backend/
        load_dotenv(dotenv_path=env_path, override=False)

        self.frontend_url: str = self._get_frontend_url()

    def _get_frontend_url(self) -> str:
        """
        Retrieve FRONTEND_URL from environment variables.

        Raises:
            ValueError: If FRONTEND_URL is not set.

        Returns:
            str: FRONTEND_URL.
        """
        # read from ./backend/.env
        url = os.getenv("FRONTEND_URL")
        if url is None:
            raise ValueError("FRONTEND_URL not set")
        return url

    def create_app(self) -> FastAPI:
        """
        Create and configure the FastAPI application.

        Returns:
            FastAPI: Configured FastAPI application instance.
        """
        app = FastAPI(title="FastAPI Backend with SQLModel")

        origins = [
            self.frontend_url,
            # add URLs of other sub-frontends or environments
        ]

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # FastAPI automatically triggers the "startup" event when the app starts.
        @app.on_event("startup")
        def on_startup() -> None:
            """
            Initialize the database and create tables when the app starts.

            Returns:
                None
            """
            Database.create_db_and_tables()

        app.include_router(item_router)
        return app
