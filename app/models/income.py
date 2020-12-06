import sqlite3
from schemas.income import IncomeCreate, IncomeGet
from datetime import datetime

db_path = 'db.db'


def create_income(income: IncomeCreate, budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        INSERT INTO income (id, description, amount,
        category, created_at, budget_id) values(NULL,?,?,?,?,?)
        """, (income.description, income.amount, income.category,
        datetime.now(),budget_id))
        con.commit()
    return income


def get_income_by_id(income_id: int, budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT description, amount, category, created_at FROM income
         WHERE id=? AND budget_id=?
        """, (income_id, budget_id))
        row = cur.fetchone()
    if not row:
        return None
    income = IncomeGet(
        id=income_id,
        description=row[0],
        amount=row[1],
        category=row[2],
        created_at=row[3],
        )
    return income


def get_all_incomes(budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT id, description, amount, category, created_at FROM income
        WHERE budget_id=?
        """, (budget_id, ))
        rows = cur.fetchall()
    if rows == []:
        return rows
    res = []
    for row in rows:
        res.append(IncomeGet(
        id=row[0],
        description=row[1],
        amount=row[2],
        category=row[3],
        created_at=row[4]
        ))
    return res


def get_incomes_in_period(budget_id: int, start_date: datetime, end_date: datetime):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT id, description, amount, category, created_at FROM income
        WHERE created_at > ? AND created_at < ? AND budget_id=?
        """, (start_date, end_date, budget_id))
        rows = cur.fetchall()
    if rows == []:
        return rows
    res = []
    for row in rows:
        res.append(IncomeGet(
            id=row[0],
            description=row[1],
            amount=row[2],
            category=row[3],
            created_at=row[4]
        ))
    return res


def edit_income(income: IncomeCreate, income_id: int, budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        UPDATE income SET description=?, amount=?,
        category=? WHERE id=? AND budget_id=?
        """, (income.description, income.amount, income.category,
        income_id, budget_id))
        con.commit()
    return income


def delete_income(income_id: int, budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        DELETE FROM income WHERE id=? AND budget_id=?
        """, (income_id, budget_id))
        con.commit()
    return income_id
