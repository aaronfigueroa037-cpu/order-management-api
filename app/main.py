from fastapi import FastAPI

app = FastAPI(title="Order Management API")

@app.get("/")
def root():
     """Health check endpoint"""
     return {"message": "Order Management API is running!"}