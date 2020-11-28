from datetime import datetime
from pydantic import BaseModel


class BudgetCreate(BaseModel):
    name: str
    amount: float

class BudgetGet(BaseModel):
    id: int
    name: str
    amount: float
    created_at: datetime

class BudgetEdit(BaseModel):
    name: str
    amount: float
