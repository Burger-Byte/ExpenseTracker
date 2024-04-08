import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
con = sqlite3.connect('expensedata.db')

from database import create_expense, get_expenses, get_categories, update_expense, delete_expense, delete_category, delete_all_expenses, delete_all_categories

### Example usage:
# create_expense('2024-03-30', 50.00, 'Groceries', 1)
# expenses = get_expenses()
# print(expenses)

# create_expense('2024-03-31', 50.00, 'Groceries', 1)
# expenses = get_expenses()
# print(expenses)

# delete_expense(1)
# expenses = get_expenses()
# print(expenses)

# delete_category(15)
# categories = get_categories()
# print(categories)

### Call delete_all_expenses function to delete all expenses
# delete_all_categories()
# print("All categories deleted successfully!")
### Call delete_all_expenses function to delete all expenses
# delete_all_expenses()
# print("All expenses deleted successfully!")

### Commit changes
con.commit()
### Close the connection
con.close()