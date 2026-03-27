"""Pydantic schemas"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Auth
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

# Items
class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pendiente"

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class ItemResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    created_at: datetime
    owner_id: int
    
    class Config:
        from_attributes = True
