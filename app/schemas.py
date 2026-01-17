from pydantic import BaseModel

class UserCreate(BaseModel):
     name: str
     email: str

class UserResponse(UserCreate):
     id: int
     name: str
     email: str

     class Config:
          from_attributes = True