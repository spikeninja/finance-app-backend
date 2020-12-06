from pydantic import BaseModel
from datetime import datetime


class ExpenseCreate(BaseModel):
    description: str
    amount: float
    category: str

class ExpenseGet(BaseModel):
    id: int
    description: str
    amount: float
    category: str
    created_at: datetime
