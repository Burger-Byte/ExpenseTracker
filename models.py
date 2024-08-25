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
    conn = sqlite3.connect('data/expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (date, amount, category, description)
        VALUES (?, ?, ?, ?)
    ''', (date, amount, category, description))
    conn.commit()
    conn.close()
