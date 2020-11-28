from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from models import users as user_model
from models.dependencies import get_current_user



router = APIRouter()

#def auth(form_data: OAuth2PasswordRequestForm = Depends()):

@router.post('/auth', response_model=user_model.TokenBase)
def auth(form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_model.get_user_by_email(email=form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect credentials.")
    if not user_model.validate_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect credentials.")
    token = user_model.create_token(user.id)
    return user_model.TokenBase(token=token)


@router.post('/register', response_model=user_model.TokenBase)
def register(user: user_model.UserCreate):
    db_user = user_model.get_user_by_email(email=user.email)
    if db_user:
        return HTTPException(status_code=400, detail="Email already exists")
    user_id = user_model.create_user(user)
    token = user_model.create_token(user_id)
    return user_model.TokenBase(token=token)


@router.get('/me', response_model=user_model.UserGet)
def me(id: int = Depends(get_current_user)):
    user = user_model.get_user_by_id(id)
    return user
