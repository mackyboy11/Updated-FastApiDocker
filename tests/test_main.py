# Simple smoke test to verify FastAPI app loads
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200

def test_docs():
    """Test /docs endpoint exists."""
    response = client.get("/docs")
    assert response.status_code == 200