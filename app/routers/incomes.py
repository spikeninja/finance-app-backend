from fastapi import APIRouter, Depends

from models import income as income_model
from models.dependencies import get_current_user


router = APIRouter()


@router.post('/')
def create_income(income: income_model.IncomeCreate, budget_id: int,
                  user_id: int = Depends(get_current_user)):
    income = income_model.create_income(income, budget_id)
    return income


@router.get('/{id}')
def get_income(id: int, budget_id: int,
               user_id: int = Depends(get_current_user)):
    income = income_model.get_income_by_id(id, budget_id)
    return income


@router.get('/')
def get_all_incomes(budget_id: int,
                    user_id: int = Depends(get_current_user)):
    incomes = income_model.get_all_incomes(budget_id)
    return incomes


@router.put('/{id}')
def get_income(id: int, budget_id: int,
               income: income_model.IncomeCreate,
               user_id: int = Depends(get_current_user)):
    edited = income_model.edit_income(income, id, budget_id)
    return edited


@router.delete('/{id}')
def delete_income(id: int, budget_id: int,
                  user_id: int = Depends(get_current_user)):
    income = income_model.delete_income(id, budget_id)
    return income
