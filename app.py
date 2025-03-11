# Expense Tracker App
#Written By: Michael Figueiredo
#Date Created: 03/10/2025
#Project: Expense Tracker App
#Last Updated: 03/11/2025

# App Design
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QTableWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView

from PyQt6.QtCore import QDate, Qt
from database import fetch_expenses, add_expense, delete_expense


class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()

    def settings(self):
        self.setGeometry(750, 300, 550, 500)
        self.setWindowTitle("Expense Tracker App")


    # Design 
    def initUI(self):
        # Create all objects
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.btn_add = QPushButton("Add Expense")
        self.btn_delete = QPushButton("Delete Expense")

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Category",
        "Amount", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.
        ResizeMode.Stretch)

        self.populate_dropdown() # Populate the dropdown

        self.btn_add.clicked.connect(self.add_expense)
        self.btn_delete.clicked.connect(self.delete_expense)

        # edit table width

        # Add widgets to a Layout (Row/Column)
        self.setup_layout()

    def setup_layout(self):
        master = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        # Row 1
        row1.addWidget(QLabel("Date"))
        row1.addWidget(self.date_box)
        row1.addWidget(QLabel("Category"))
        row1.addWidget(self.dropdown)

        # Row 2
        row2.addWidget(QLabel("Amount"))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel("Description"))
        row2.addWidget(self.description)
        row2.addWidget(self.btn_add)
        row3.addWidget(self.btn_delete)

        master.addLayout(row1)
        master.addLayout(row2)
        master.addLayout(row3)
        master.addWidget(self.table)

        self.setLayout(master)



        # Row 3


    def populate_dropdown(self):
        categories = ["Groceries","Eating out", "Rent", "Utilities", "Transportation", "Terra Schools", 
        "Violin", "Clarinet", "Bata", "Bob Mover Lessons", "Gas", "Miscellaneous"]
        self.dropdown.addItems(categories)

    def load_table_data(self):
        expenses = fetch_expenses()
        self.table.setRowCount(0)
        for row_idx, expense in enumerate(expenses):
            self.table.insertRow(row_idx)
            for col_idx, data in enumerate(expense):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    
    def clear_inputs(self):
        self.date_box.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()


    def add_expense(self):
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText() # QCombobox
        amount = self.amount.text() # QLineEdit
        description = self.description.text()

        if not amount or not description:
            QMessageBox.warning(self, "Input Error", "Amount and Description cannot be empty")
            return
        
        if add_expense(date, category, amount, description):
            self.load_table_data()
            # Clear inputs
            self.clear_inputs()
        else:
            QMessageBox.critical(self, "Error", "Could not add expense")


    def delete_expense(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Uh oh", "You need to select a row to delete")
            return

        expense_id = int(self.table.item(selected_row, 0).text())
        confirm = QMessageBox.question(self, "Confirm",
         "Are you sure you want to delete?", QMessageBox.StandardButton.Yes | QMessageBox.
         StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes and delete_expense(expense_id):
            self.load_table_data()
