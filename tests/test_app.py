# tests/test_app.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict():
    response = client.post(
        "/predict",
        json={"data": [[8.3252, 41, 6.984127, 1.02381, 322, 2.555556, 37.88, -122.23], 
                       [8.3014, 21, 6.238137, 1.072314, 240, 2.109842, 37.86, -122.22]]}
    )
    assert response.status_code == 200
    assert "predictions" in response.json()
    assert len(response.json()["predictions"]) == 2

def test_predict_invalid_input():
    response = client.post(
        "/predict",
        json={"data": [[8.3252, 41, 6.984127]]}  # Invalid input
    )
    assert response.status_code == 400
