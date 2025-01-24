from fastapi import FastAPI

app = FastAPI()

PROCESSED_ORDERS = []  # Simulates a database in memory

@app.post("/process-order")
def process_order(order: dict):
    """
    Endpoint to process an order received from Microservice 1.
    """
    PROCESSED_ORDERS.append(order)  # Save to in-memory list
    return {"message": "Order processed successfully", "order": order}
