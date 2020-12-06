from fastapi import APIRouter, Depends

from models import expense as expense_model
from models.dependencies import get_current_user


router = APIRouter()


@router.post('/')
def create_expense(expense: expense_model.ExpenseCreate, budget_id: int,
                  user_id: int = Depends(get_current_user)):
    expense = expense_model.create_expense(expense, budget_id)
    return expense


@router.get('/{id}')
def get_expense(id: int, budget_id: int,
               user_id: int = Depends(get_current_user)):
    expense = expense_model.get_expense_by_id(id, budget_id)
    return expense


@router.get('/')
def get_all_expenses(budget_id: int,
                    user_id: int = Depends(get_current_user)):
    expenses = expense_model.get_all_expenses(budget_id)
    return expenses


@router.put('/{id}')
def get_expense(id: int, budget_id: int,
               expense: expense_model.ExpenseCreate,
               user_id: int = Depends(get_current_user)):
    edited = expense_model.edit_expense(expense, id, budget_id)
    return edited


@router.delete('/{id}')
def delete_expense(id: int, budget_id: int,
                  user_id: int = Depends(get_current_user)):
    expense = expense_model.delete_expense(id, budget_id)
    return expense
