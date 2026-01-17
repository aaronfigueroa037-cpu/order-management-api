from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
     # Check if email already exists
     existing = db.query(models.User).filter(models.User.email == user.email).first()
     if existing:
          raise HTTPException(status_code=400, detail="Email already registered")

     db_user = models.User(name=user.name, email=user.email)
     db.add(db_user)
     db.commit()
     db.refresh(db_user)
     return db_user

@router.get("/", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
     return db.query(models.User).all()