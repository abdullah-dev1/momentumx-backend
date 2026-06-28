from pydantic import BaseModel
from typing import Optional
from datetime import date

class HabitCreate(BaseModel):
    title: str
    emoji: str = "⭐"

class HabitUpdate(BaseModel):
    title: Optional[str] = None
    emoji: Optional[str] = None
    is_done: Optional[bool] = None

class HabitResponse(BaseModel):
    id: int
    title: str
    emoji: str
    is_done: bool
    date: Optional[date]

    class Config:
        from_attributes = True