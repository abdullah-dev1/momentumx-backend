from pydantic import BaseModel
from typing import List, Any
from datetime import datetime

class WorkoutCreate(BaseModel):
    name: str = "Workout"
    duration_seconds: int = 0
    total_volume: float = 0
    exercises: List[Any] = []

class WorkoutResponse(BaseModel):
    id: int
    name: str
    duration_seconds: int
    total_volume: float
    exercises: List[Any]
    created_at: datetime

    class Config:
        from_attributes = True