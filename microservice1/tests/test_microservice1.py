from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/create-order", json={"order_id": 1, "item": "Book", "quantity": 10})
    assert response.status_code == 200
    assert response.json()["order"]["item"] == "Book"
