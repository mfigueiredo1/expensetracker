# Expense Tracker App
#Written By: Michael Figueiredo
#Date Created: 03/10/2025
#Project: Expense Tracker App
#Last Updated: 03/11/2025
import sys
import os
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

def init_db(db_name):
    # get the correct database path
    if getattr(sys, 'frozen', False):
        # IF the app is running as a frozen executable (e.g, bundeled with PyInstaller)
        db_path = os.path.join(os.path.dirname(sys.executable), 'expenses.db')
    else:
        # If running in a development environment (e.g., directly from the source code)
        db_path = os.path.join(os.path.dirname(__file__), 'expenses.db')

    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName(db_path)
    
    if not database.open():
        return False

    query = QSqlQuery()
    query.exec("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
        """)

    return True
        

        
def fetch_expenses():
    query = QSqlQuery("SELECT * FROM expenses ORDER BY date DESC")
    expenses = []
    while query.next():
        row = [query.value(i) for i in range(5)]
        expenses.append(row)
    return expenses

def add_expenses(date, category, amount, description):
    query = QSqlQuery()
    query.prepare("""
                INSERT INTO expenses (date, category, amount, description)
                VALUES (?, ?, ?, ?)
                """)

    query.addBindValue(date)
    query.addBindValue(category)
    query.addBindValue(amount)
    query.addBindValue(description)

    return query.exec()

def delete_expenses(expense_id):
    query = QSqlQuery()
    query.prepare("DELETE FROM expenses WHERE id = ?")
    query.addBindValue(expense_id)
    return query.exec()
