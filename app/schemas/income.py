from pydantic import BaseModel
from datetime import datetime


class IncomeCreate(BaseModel):
    description: str
    amount: float
    category: str

class IncomeGet(BaseModel):
    id: int
    description: str
    amount: float
    category: str
    created_at: datetime
