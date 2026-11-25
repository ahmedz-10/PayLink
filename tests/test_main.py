import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "PayLink application is running!"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["application"] == "running"
