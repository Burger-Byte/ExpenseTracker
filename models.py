# models.py

import sqlite3

def setup_database():
    conn = sqlite3.connect('data/expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            category TEXT,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(date, amount, category, description):
    # Connect to the database
    conn = sqlite3.connect('data/expenses.db')
    cursor = conn.cursor()

    # Add the expense to the database
    cursor.execute('INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)',
                   (date, amount, category, description))
    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    print(f"Expense added: {date}, {amount}, {category}, {description}")


def get_expenses():
    try:
        conn = sqlite3.connect('data/expenses.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
        expenses = cursor.fetchall()
        conn.close()
        return expenses
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"General error: {e}")
        return []