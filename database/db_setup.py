import sqlite3

conn = sqlite3.connect('secrets.db')
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   email TEXT UNIQUE,
                   hashed_password TEXT,
                   salt TEXT
               )''')
cursor.execute('''
                CREATE TABLE IF NOT EXISTS secrets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    username TEXT,
                    password TEXT,
                    user_id INTEGER
                )''')

conn.commit()
conn.close()