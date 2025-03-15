from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Expense
from app.chatbot import ask_ai

router = APIRouter()

@router.post("/add_expense/")
async def add_expense(user_id: int, category: str, amount: float, db: Session = Depends(get_db)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than zero")

    new_expense = Expense(user_id=user_id, category=category, amount=amount)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)  # Ensure new data is returned
    return {"message": "Expense added!", "expense": new_expense.id}

@router.get("/get_expenses/")
async def get_expenses(user_id: int, db: Session = Depends(get_db)):
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found for this user")
    return {"expenses": expenses}

@router.post("/chatbot/")
async def chatbot_query(query: str):
    response = ask_ai(query)
    return {"response": response}
