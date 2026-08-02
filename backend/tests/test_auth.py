import os
import asyncio

# Test configuration: use in-memory SQLite for tests and set test environment
os.environ.setdefault("ENVIRONMENT", "test")
os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///:memory:")

from fastapi.testclient import TestClient
from app.main import app
from app.db.session import init_db

# Initialize in-memory database tables for tests
asyncio.run(init_db())

client = TestClient(app)

def test_register_and_login():
    # Register
    payload = {"email": "test@example.com", "password": "secret", "full_name": "Test User"}
    r = client.post("/api/v1/auth/register", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert data["email"] == "test@example.com"

    # Login
    r2 = client.post("/api/v1/auth/token", data={"username": "test@example.com", "password": "secret"})
    assert r2.status_code == 200
    tokens = r2.json()
    assert "access_token" in tokens
    assert "refresh_token" in tokens
