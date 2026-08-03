import os

# Test configuration: use in-memory SQLite for tests and set test environment if not already set
os.environ.setdefault("ENVIRONMENT", "test")
os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///:memory:")

import asyncio
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import init_db

# Initialize in-memory database tables for tests
asyncio.run(init_db())

client = TestClient(app)


def test_register_and_login_and_refresh_and_me():
    # Register
    payload = {"email": "test@example.com", "password": "secret", "full_name": "Test User"}
    r = client.post("/api/v1/auth/register", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["email"] == "test@example.com"

    # Login
    r2 = client.post(
        "/api/v1/auth/token", data={"username": "test@example.com", "password": "secret"}
    )
    assert r2.status_code == 200
    tokens = r2.json()
    assert "access_token" in tokens
    assert "refresh_token" in tokens

    # Refresh
    r3 = client.post(
        "/api/v1/auth/refresh", json={"refresh_token": tokens["refresh_token"]}
    )
    assert r3.status_code == 200
    refreshed = r3.json()
    assert "access_token" in refreshed
    assert "refresh_token" in refreshed

    # Me endpoint
    headers = {"Authorization": f"Bearer {tokens['access_token']}"}
    r4 = client.get("/api/v1/auth/me", headers=headers)
    assert r4.status_code == 200
    me = r4.json()
    assert me["email"] == "test@example.com"


def test_refresh_with_invalid_token():
    r = client.post("/api/v1/auth/refresh", json={"refresh_token": "invalid.token.here"})
    assert r.status_code == 401


def test_refresh_with_expired_token():
    from datetime import timedelta
    from app.core.security import create_refresh_token

    expired = create_refresh_token(subject="1", expires_delta=timedelta(seconds=-60))
    r = client.post("/api/v1/auth/refresh", json={"refresh_token": expired})
    assert r.status_code == 401


def test_me_missing_token():
    r = client.get("/api/v1/auth/me")
    assert r.status_code == 401


def test_me_invalid_token():
    headers = {"Authorization": "Bearer invalidtoken"}
    r = client.get("/api/v1/auth/me", headers=headers)
    assert r.status_code == 401
