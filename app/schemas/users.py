from datetime import timestamp
from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: timestamp

class UserGet(BaseModel):
    id: int
    name: str
    email: str
