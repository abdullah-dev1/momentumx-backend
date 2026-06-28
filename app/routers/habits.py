from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from app.database import get_db
from app.models.habit import Habit
from app.schemas.habit import HabitCreate, HabitUpdate, HabitResponse
from app.core.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/habits", tags=["Habits"])

@router.get("/", response_model=List[HabitResponse])
def get_habits(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Habit).filter(Habit.user_id == current_user.id).all()

@router.post("/", response_model=HabitResponse)
def create_habit(
    data: HabitCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = Habit(
        user_id=current_user.id,
        title=data.title,
        emoji=data.emoji,
        date=date.today()
    )
    db.add(habit)
    db.commit()
    db.refresh(habit)
    return habit

@router.put("/{habit_id}", response_model=HabitResponse)
def update_habit(
    habit_id: int,
    data: HabitUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = db.query(Habit).filter(
        Habit.id == habit_id,
        Habit.user_id == current_user.id
    ).first()
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(habit, field, value)
    db.commit()
    db.refresh(habit)
    return habit

@router.delete("/{habit_id}")
def delete_habit(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = db.query(Habit).filter(
        Habit.id == habit_id,
        Habit.user_id == current_user.id
    ).first()
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    db.delete(habit)
    db.commit()
    return {"message": "Habit deleted"}

@router.post("/sync", response_model=List[HabitResponse])
def sync_habits(
    habits: List[HabitCreate],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db.query(Habit).filter(
        Habit.user_id == current_user.id,
        Habit.date == date.today()
    ).delete()
    new_habits = [
        Habit(
            user_id=current_user.id,
            title=h.title,
            emoji=h.emoji,
            date=date.today()
        ) for h in habits
    ]
    db.add_all(new_habits)
    db.commit()
    return db.query(Habit).filter(Habit.user_id == current_user.id).all()