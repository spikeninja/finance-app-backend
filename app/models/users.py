import os, hashlib, random, string, jwt, sqlite3

from schemas.users import UserCreate, UserGet, TokenBase, UserDetailGet
from datetime import datetime, timedelta


SECRET_KEY = os.getenv('SECRET_KEY', 'default_value')
db_path = 'db.db'


def validate_password(password:str, hashed_password:str):
    p = hashlib.sha256(password.encode()).hexdigest()
    return p == hashed_password


def create_token(id: int):
    """
    Generates the auth_token
    :return: string
    """
    payload = {
        "sub": id,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(days=3)
    }
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm='HS256'
    )


def decode_token(token: str):
    """
    Decodes the auth token.
    :param token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(token, SECRET_KEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return "Signature expired. Please log in again."
    except jwt.InvalidTokenError:
        return "Invalid token. Please log in again."


def get_user_by_id(id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""SELECT name, email FROM
            users WHERE id=?
        """, (id,))
        res = cur.fetchone()
    user_json = {
        "id": id,
        "name": res[0],
        "email": res[1]
    }
    user = UserGet(**user_json)
    return user



def get_user_by_email(email: str):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
            SELECT id, name, password FROM
            users WHERE email=?
        """, (email,))
        res = cur.fetchone()
    if not res:
        return None
    user_json = {
        "id": res[0],
        "name": res[1],
        "email": email,
        "password": res[2]
    }
    user = UserDetailGet(**user_json)
    return user


def create_user(user: UserCreate):
    hashed_password = hashlib.sha256(user.password.encode('utf-8')).hexdigest()
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        INSERT INTO users(id, name, email, password, created_at)
        VALUES (NULL, ?, ?, ?, ?)""",
        (user.name, user.email, hashed_password, datetime.now())
        )
        con.commit()
        id = cur.lastrowid
    return id
