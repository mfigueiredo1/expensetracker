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