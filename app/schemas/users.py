from datetime import datetime
from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: datetime

class UserGet(BaseModel):
    id: int
    name: str
    email: str
