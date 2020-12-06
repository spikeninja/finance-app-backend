import sqlite3
from schemas.expense import ExpenseCreate, ExpenseGet
from datetime import datetime

db_path = 'db.db'


def create_expense(expense: ExpenseCreate, budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        INSERT INTO expense (id, description, amount,
        category, created_at, budget_id) values(NULL,?,?,?,?,?)
        """, (expense.description, expense.amount, expense.category,
        datetime.now(),budget_id))
        con.commit()
    return expense


def get_expense_by_id(expense_id: int, budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT description, amount, category, created_at FROM expense
         WHERE id=? AND budget_id=?
        """, (expense_id, budget_id))
        row = cur.fetchone()
    if not row:
        return None
    expense = ExpenseGet(
        id=expense_id,
        description=row[0],
        amount=row[1],
        category=row[2],
        created_at=row[3],
        )
    return expense


def get_all_expenses(budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT id, description, amount, category, created_at FROM expense
        WHERE budget_id=?
        """, (budget_id, ))
        rows = cur.fetchall()
    if rows == []:
        return rows
    res = []
    for row in rows:
        res.append(ExpenseGet(
        id=row[0],
        description=row[1],
        amount=row[2],
        category=row[3],
        created_at=row[4]
        ))
    return res


def get_expenses_in_period(budget_id: int, start_date: datetime, end_date: datetime):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        SELECT id, description, amount, category, created_at FROM expense
        WHERE created_at > ? AND created_at < ? AND budget_id=?
        """, (start_date, end_date, budget_id))
        rows = cur.fetchall()
    if rows == []:
        return rows
    res = []
    for row in rows:
        res.append(ExpenseGet(
            id=row[0],
            description=row[1],
            amount=row[2],
            category=row[3],
            created_at=row[4]
        ))
    return res


def edit_expense(expense: ExpenseCreate, expense_id: int, budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        UPDATE expense SET description=?, amount=?,
        category=? WHERE id=? AND budget_id=?
        """, (expense.description, expense.amount, expense.category,
        expense_id, budget_id))
        con.commit()
    return expense


def delete_expense(expense_id: int, budget_id: int):
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute("""
        DELETE FROM expense WHERE id=? AND budget_id=?
        """, (expense_id, budget_id))
        con.commit()
    return expense_id
