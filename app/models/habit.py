from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    emoji = Column(String, default="⭐")
    is_done = Column(Boolean, default=False)
    date = Column(Date, nullable=True)

    user = relationship("User", back_populates="habits")