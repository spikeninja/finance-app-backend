import os
import sys
import sqlite3

from schemas.budget import BudgetGet, BudgetCreate, BudgetEdit
from datetime import datetime

sys.path.append('.')

db_path = 'db.db'
SECRET_KEY = os.getenv('SECRET_KEY', 'default_value')



def create_budget(budget: BudgetCreate, user_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        INSERT INTO budget
        (id, name, amount, created_at, user_id)
        VALUES (NULL,?,?,?,?)
        """,
        (budget.name, budget.amount, datetime.now(), user_id))
        con.commit()
        id = cur.lastrowid
    return id


def get_all_budgets(user_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT id, name, amount, created_at FROM budget
        WHERE user_id=?
        """, (user_id,))
        rows = cur.fetchall()
    if rows == []:
        return None
    res = []
    for e in rows:
        row_json = {
            "id": e[0],
            "name": e[1],
            "amount": e[2],
            "created_at": e[3]
        }
        res.append(BudgetGet(**row_json))
    return res


def get_budget_by_id(budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT name, amount, created_at FROM
        budget WHERE id=?
        """, (budget_id,))
        row = cur.fetchone()
    if not row:
        return None
    row_json = {
        "id": budget_id,
        "name": row[0],
        "amount": row[1],
        "created_at": row[2]
    }
    return BudgetGet(**row_json)


def edit_budget(budget: BudgetEdit, budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        UPDATE budget SET
        name=?, amount=? WHERE id=?
        """, (budget.name, budget.amount, budget_id))
        con.commit()
    return budget


def delete_budget_by_id(budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        DELETE FROM budget WHERE id=?
        """, (budget_id,))
        con.commit()
    return budget_id
