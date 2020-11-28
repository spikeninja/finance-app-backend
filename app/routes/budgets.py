from fastapi import APIRouter, Depends

from models import budget as budget_model
from models.dependencies import get_current_user

router = APIRouter()


@router.get('/')
def get_all_budgets(user_id: int = Depends(get_current_user)):
    budgets = budget_model.get_all_budgets(user_id)
    return budgets


@router.get('/{id}', response_model=budget_model.BudgetGet)
def get_budget_by_id(id: int, user_id: int = Depends(get_current_user)):
    budget = budget_model.get_budget_by_id(id, user_id)
    return budget


@router.post('/')
def create_budget(budget: budget_model.BudgetCreate,
                  user_id: int = Depends(get_current_user)):
    id = budget_model.create_budget(budget, user_id)
    return id


@router.put('/{id}', response_model=budget_model.BudgetEdit)
def update_budget(budget: budget_model.BudgetEdit,
                  id: int, user_id: int = Depends(get_current_user)):
    budget_edited = budget_model.edit_budget(budget, id, user_id)
    return budget_edited


@router.delete('/{id}')
def delete_budget(id: int, user_id: int = Depends(get_current_user)):
    budget_id = budget_model.delete_budget_by_id(id, user_id)
    return budget_id
