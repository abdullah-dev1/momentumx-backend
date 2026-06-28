from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, default="Workout")
    duration_seconds = Column(Integer, default=0)
    total_volume = Column(Float, default=0)
    exercises = Column(JSON, default=[])
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="workouts")