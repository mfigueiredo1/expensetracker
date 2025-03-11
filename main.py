# Expense Tracker App
#Written By: Michael Figueiredo
#Date Created: 03/10/2025
#Project: Expense Tracker App
#Last Updated: 03/11/2025

# Running the App
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from database import init_db
from app import ExpenseApp

def main():
    app = QApplication(sys.argv)

    if not init_db("expenses.db"):
        QMessageBox.critical(None, "Error", "could not load your database")
    window = ExpenseApp()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()