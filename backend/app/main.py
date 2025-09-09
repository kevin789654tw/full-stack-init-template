from app.core.app import AppFactory
from fastapi import FastAPI


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: Configured FastAPI application instance.
    """
    return AppFactory().create_app()
