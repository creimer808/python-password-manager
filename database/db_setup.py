import sqlite3

conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT,
                   last_name TEXT,
                   email TEXT UNIQUE,
                   hashed_password TEXT,
                   salt TEXT
               )''')

conn.commit()
conn.close()