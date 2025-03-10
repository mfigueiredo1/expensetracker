# App Design
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QTableWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView

from PyQt6.QtCore import QDate, Qt

class ExpenseApp(QWidget):
    def _init_(self):
        super()._init_()
        self.settings()

    def settings(self):
        self.setGeometry(750, 300, 550, 500)
        self.setWindowTitle("Expense Tracker App")