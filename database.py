import sqlite3
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


# Commit changes
con.commit()
# Close the connection
con.close()