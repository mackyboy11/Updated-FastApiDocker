from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_read_root():
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code in (200, 307)

def test_docs():
    """Test /docs endpoint exists."""
    response = client.get("/docs")
    assert response.status_code == 200

def test_openapi_schema():
    """Test OpenAPI schema endpoint."""
    response = client.get("/openapi.json")
    assert response.status_code == 200