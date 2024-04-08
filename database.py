import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
con = sqlite3.connect("expensedata.db")
# Create a cursor object
cur = con.cursor()

    
# Execute SQL queries
cur.execute("""CREATE TABLE IF NOT EXISTS Expenses 
            (
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            date TEXT, 
            amount NUMERIC, 
            description TEXT, 
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES Categories(category_id)
            )
            """)
cur.execute("""CREATE TABLE IF NOT EXISTS Categories 
            (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT
            )
            """)

# CRUD functions for main
def create_expense(date, amount, description, category_id):
    try:
        conn = sqlite3.connect('expensedata.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO Expenses (date, amount, description, category_id) VALUES (?, ?, ?, ?)",
                    (date, amount, description, category_id))
        conn.commit()
    except sqlite3.Error as e:
        print("Error inserting expense:", e)
    finally:
        if conn:
            conn.close()

def get_expenses():
    expenses = []
    try:
        conn = sqlite3.connect('expensedata.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Expenses")
        expenses = cur.fetchall()
    except sqlite3.Error as e:
        print("Error fetching expenses:", e)
    finally:
        if conn:
            conn.close()
    return expenses

def get_categories():
    categories= []
    try:
        conn = sqlite3.connect('expensedata.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Categories")
        expenses = cur.fetchall()
    except sqlite3.Error as e:
        print("Error fetching categories:", e)
    finally:
        if conn:
            conn.close()
    return categories

def update_expense(expense_id, date, amount, description, category_id):
    try:
        conn = sqlite3.connect('expensedata.db')
        cur = conn.cursor()
        cur.execute("UPDATE Expenses SET date=?, amount=?, description=?, category_id=? WHERE expense_id=?",
                    (date, amount, description, category_id, expense_id))
        conn.commit()
    except sqlite3.Error as e:
        print("Error updating expense:", e)
    finally:
        if conn:
            conn.close()

def delete_expense(expense_id):
    try:
        conn = sqlite3.connect('expensedata.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM Expenses WHERE expense_id=?", (expense_id,))
        conn.commit()
    except sqlite3.Error as e:
        print("Error deleting expense:", e)
    finally:
        if conn:
            conn.close()

def delete_category(category_id):
    try:
        conn = sqlite3.connect('expensedata.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM Categories WHERE category_id=?", (category_id,))
        conn.commit()
    except sqlite3.Error as e:
        print("Error deleting category:", e)
    finally:
        if conn:
            conn.close()

def delete_all_expenses():
    try:
        conn = sqlite3.connect('expensedata.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM Expenses")
        conn.commit()
    except sqlite3.Error as e:
        print("Error deleting all expenses:", e)
    finally:
        if conn:
            conn.close()

def delete_all_categories(expense_id):
    try:
        conn = sqlite3.connect('expensedata.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM Categories")
        conn.commit()
    except sqlite3.Error as e:
        print("Error deleting categories:", e)
    finally:
        if conn:
            conn.close()

def generate_pie_chart():
    # Get expenses by category
    expenses_by_category = calculate_expenses_by_category()

    # Calculate total expenses
    total_expenses = sum(expenses_by_category.values())

    # Get income
    income = get_income()

    # Calculate remaining budget (income - expenses)
    remaining_budget = income - total_expenses

    # Data for the pie chart
    labels = expenses_by_category.keys()
    sizes = expenses_by_category.values()
    explode = [0.1] * len(labels)  # Explode all slices for better visualization

    # Add a category for remaining budget if it's positive
    if remaining_budget > 0:
        labels += ['Remaining Budget']
        sizes += [remaining_budget]
        explode += [0.1]

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title('Expenses by Category')

    # Show the pie chart
    plt.show()

def calculate_expenses_by_category():
    # Connect to the database and query expenses by category
    expenses_by_category = {}  # Dictionary to store expenses by category
    # Execute SQL query to retrieve expenses by category
    # For example:
    # SELECT category_id, SUM(amount) FROM Expenses GROUP BY category_id
    # Iterate through the results and populate the expenses_by_category dictionary
    return expenses_by_category

def get_income():
    # Connect to the database and retrieve income from the appropriate table or source
    # Execute SQL query or call a function to get the income
    # For example:
    # SELECT income FROM IncomeTable
    return income



# Commit changes
con.commit()
# Close the connection
con.close()