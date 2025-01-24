from fastapi import FastAPI

app = FastAPI()

PROCESSED_ORDERS = []

@app.post("/process-order")
def process_order(order: dict):
    PROCESSED_ORDERS.append(order)
    return {"message": "Order processed successfully", "order": order}
