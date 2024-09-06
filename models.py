# models.py

import sqlite3
import logging

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
    try:
        conn = sqlite3.connect('data/expenses.db')
        cursor = conn.cursor()

        # Check if the category exists, if not, add it to the categories table
        if not category_exists(category):
            logging.info(f"Category '{category}' does not exist. Adding it to the categories list.")
            cursor.execute('INSERT INTO categories (name) VALUES (?)', (category,))
            conn.commit()

        # Add the expense to the expenses table
        cursor.execute('INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)',
                       (date, amount, category, description))
        conn.commit()
        conn.close()

        logging.info(f"Expense added: {date}, {amount}, {category}, {description}")
        
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    except Exception as e:
        logging.error(f"General error: {e}")


def get_expenses():
    try:
        conn = sqlite3.connect('data/expenses.db')  # Make sure your database path is correct
        cursor = conn.cursor()

        # Get all expenses, ordered by date (latest first)
        cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
        expenses = cursor.fetchall()
        conn.close()

        return expenses
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return []
    except Exception as e:
        logging.error(f"General error: {e}")
        return []
    
def get_expense_reports():
    try:
        conn = sqlite3.connect('data/expenses.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT category, SUM(amount) as total
            FROM expenses
            GROUP BY category
        ''')
        reports = cursor.fetchall()
        conn.close()

        # Convert to a list of dictionaries for easier usage
        report_list = [{"category": row[0], "total": row[1]} for row in reports]
        return report_list
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    except Exception as e:
        print(f"General error: {e}")
        return []
    
def set_budget(category, amount):
    try:
        conn = sqlite3.connect('data/expenses.db')
        cursor = conn.cursor()
        
        # Create a table for budgets if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                amount REAL
            )
        ''')
        
        # Insert the new budget or update an existing one
        cursor.execute('''
            INSERT OR REPLACE INTO budgets (category, amount) VALUES (?, ?)
        ''', (category, amount))
        
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    except Exception as e:
        logging.error(f"General error: {e}")


def setup_default_categories():
    default_categories = ['Groceries', 'Transport', 'Entertainment', 'Health', 'Education']
    
    try:
        conn = sqlite3.connect('data/expenses.db')
        cursor = conn.cursor()

        # Create the categories table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE
            )
        ''')

        # Insert the default categories if they don't already exist
        for category in default_categories:
            cursor.execute('''
                INSERT OR IGNORE INTO categories (name) VALUES (?)
            ''', (category,))

        conn.commit()
        conn.close()
        logging.info("Default categories set up.")
        
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    except Exception as e:
        logging.error(f"General error: {e}")

# Function to get all categories
def get_categories():
    try:
        conn = sqlite3.connect('data/expenses.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM categories')
        categories = cursor.fetchall()
        conn.close()
        return [category[0] for category in categories]  # Return a list of category names
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return []
    except Exception as e:
        logging.error(f"General error: {e}")
        return []

def category_exists(category):
    try:
        conn = sqlite3.connect('data/expenses.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(1) FROM categories WHERE name = ?', (category,))
        exists = cursor.fetchone()[0] > 0
        conn.close()
        return exists
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
        return False
    except Exception as e:
        logging.error(f"General error: {e}")
        return False
    
# Function to add a category
def add_category(category_name):
    try:
        conn = sqlite3.connect('data/expenses.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO categories (name) VALUES (?)', (category_name,))
        conn.commit()
        conn.close()
        logging.info(f"Category '{category_name}' added.")
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    except Exception as e:
        logging.error(f"General error: {e}")

# Function to delete a category
def delete_category(category_name):
    try:
        conn = sqlite3.connect('data/expenses.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM categories WHERE name = ?', (category_name,))
        conn.commit()
        conn.close()
        logging.info(f"Category '{category_name}' deleted.")
    except sqlite3.Error as e:
        logging.error(f"Database error: {e}")
    except Exception as e:
        logging.error(f"General error: {e}")