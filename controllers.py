from kivy.uix.screenmanager import Screen
from models import add_expense, set_budget, get_expense_reports, get_expenses

class AddExpenseScreen(Screen):
    def submit_expense(self, date, amount, category, description):
        try:
            # Convert amount to float and attempt to add expense to database
            amount = float(amount)
            add_expense(date, amount, category, description)
            print(f"Expense added: {date}, {amount}, {category}, {description}")
        except ValueError:
            print("Error: Invalid amount. Please enter a valid number.")
        except Exception as e:
            print(f"Error adding expense: {e}")

class ViewExpensesScreen(Screen):
    def on_enter(self):
        expenses = get_expenses()
        for expense in expenses:
            print(expense)  # Ideally, update a list widget or similar display method

class SetBudgetScreen(Screen):
    def submit_budget(self, category, amount):
        try:
            amount = float(amount)
            set_budget(category, amount)
            print(f"Budget set: {category} with amount {amount}")
        except ValueError:
            print("Error: Invalid budget amount. Please enter a valid number.")
        except Exception as e:
            print(f"Error setting budget: {e}")

class ViewReportsScreen(Screen):
    def on_enter(self):
        reports = get_expense_reports()
        for report in reports:
            print(report)  # Ideally, this would update a graphical report view

