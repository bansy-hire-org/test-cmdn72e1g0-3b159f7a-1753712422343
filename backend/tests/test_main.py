from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

@pytest.fixture
def mock_openai_response(monkeypatch):
    class MockCompletion:
        @staticmethod
        def create(**kwargs):
            return {"choices": [{"text": "Negative"}]}
    monkeypatch.setattr('main.openai.Completion', MockCompletion)

def test_create_complaint(mock_openai_response):
    response = client.post("/complaints", json={"complaint": "The service was terrible!"})
    assert response.status_code == 200
    assert response.json() == {"message": "Complaint submitted and analyzed!"}

def test_create_complaint_empty():
    response = client.post("/complaints", json={"complaint": ""})
    assert response.status_code == 200
    assert response.json() == {"message": "Complaint submitted and analyzed!"} # BUG: Should handle empty complaints better

def test_get_complaint_not_found():
    response = client.get("/complaints/nonexistent_id")
    assert response.status_code == 404
    assert response.json() == {"detail": "Complaint not found"}