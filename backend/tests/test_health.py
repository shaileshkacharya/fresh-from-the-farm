import os
# Ensure the application knows it's in test mode to avoid startup DB initialization
os.environ.setdefault("ENVIRONMENT", "test")

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
