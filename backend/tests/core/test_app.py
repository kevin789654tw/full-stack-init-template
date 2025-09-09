# Ignore Bandit warning B101 (assert used) in this file.
# For reference on usage, see:
# https://github.com/trunk-io/flake-factory/blob/275f85ee4ccb443fe7062ff8042bb1faf4d9935b/python/pytest/random_test.py#L1

# trunk-ignore-all(bandit/B101)
import tempfile
from pathlib import Path

import pytest
from app.core.app import AppFactory
from app.db.database import Database
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from fastapi.testclient import TestClient


def test_appfactory_init(monkeypatch):
    monkeypatch.setenv("FRONTEND_URL", "http://localhost:3000")
    factory = AppFactory()
    assert factory.frontend_url == "http://localhost:3000"


def test_appfactory_missing_env(monkeypatch):
    monkeypatch.delenv("FRONTEND_URL", raising=False)

    with tempfile.TemporaryDirectory() as tmpdir:
        env_path = Path(tmpdir) / ".env"
        env_path.touch()

        with pytest.raises(ValueError):
            AppFactory(env_path=env_path)


def test_create_app_instance(monkeypatch):
    monkeypatch.setenv("FRONTEND_URL", "http://localhost:3000")
    factory = AppFactory()
    app = factory.create_app()
    assert isinstance(app, FastAPI)
    assert app.title == "FastAPI Backend with SQLModel"
    route_tags = [
        r.tags for r in app.router.routes if isinstance(r, APIRoute) and r.tags
    ]
    flat_tags = [tag for tags in route_tags for tag in tags]  # flatten
    assert "Items" in flat_tags


def test_cors_middleware_settings(monkeypatch):
    monkeypatch.setenv("FRONTEND_URL", "http://localhost:3000")
    factory = AppFactory()
    app = factory.create_app()

    cors = [m for m in app.user_middleware if m.cls == CORSMiddleware]
    assert len(cors) == 1

    assert cors[0].kwargs["allow_origins"] == [factory.frontend_url]
    assert cors[0].kwargs["allow_methods"] == ["*"]
    assert cors[0].kwargs["allow_headers"] == ["*"]
    assert cors[0].kwargs["allow_credentials"] is True


def test_startup_event(monkeypatch):
    monkeypatch.setenv("FRONTEND_URL", "http://localhost:3000")
    called = {}

    def fake_create_db_and_tables():
        called["yes"] = True

    monkeypatch.setattr(Database, "create_db_and_tables", fake_create_db_and_tables)

    factory = AppFactory()
    app = factory.create_app()
    with TestClient(app):
        pass  # triggers startup event

    assert called.get("yes") is True
