# Expense Tracker App
#Written By: Michael Figueiredo
#Date Created: 03/10/2025
#Project: Expense Tracker App
#Last Updated: 03/10/2025

# Running the App
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from app import ExpenseApp

def main():
    app = QApplication(sys.argv)
    window = ExpenseApp()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()