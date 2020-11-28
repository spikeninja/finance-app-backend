from datetime import datetime
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserGet(BaseModel):
    id: int
    name: str
    email: str

class UserDetailGet(UserGet):
    password: str

class TokenBase(BaseModel):
    token: str
