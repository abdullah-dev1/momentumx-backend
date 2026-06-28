from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    goal: Optional[str] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    calorie_goal: Optional[int] = None
    water_goal: Optional[float] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    goal: str
    weight: Optional[float]
    height: Optional[float]
    calorie_goal: int
    water_goal: float
    streak_days: int
    created_at: datetime

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
class ForgotPasswordRequest(BaseModel):
    email: EmailStr