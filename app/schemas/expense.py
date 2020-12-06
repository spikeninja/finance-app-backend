from pydantic import BaseModel


class ExpenseCreate(BaseModel):
    description: str
    amount: float
    category: str

class IncomeGet(BaseModel):
    id: int
    description: str
    amount: float
    category: str
    created_at: datetime
