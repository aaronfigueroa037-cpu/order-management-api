from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routes import users

app = FastAPI(title="Order Management API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
     return {"message": "Order Management API is running!"}

app.include_router(users.router)