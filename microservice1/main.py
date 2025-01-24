from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

ORDERS = []  # Simulates a database in memory

MICROSERVICE_2_URL = "http://microservice2.default.svc.cluster.local:8000/process-order"  # Replace with service name in Kubernetes

@app.post("/create-order")
def create_order(order_id: int, item: str, quantity: int):
    """
    Endpoint to create an order and send it to Microservice 2 for processing.
    """
    order = {"order_id": order_id, "item": item, "quantity": quantity}
    ORDERS.append(order)  # Save to in-memory list
    try:
        response = requests.post(MICROSERVICE_2_URL, json=order)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to send order: {e}")
    return {"message": "Order created and sent", "order": order}
