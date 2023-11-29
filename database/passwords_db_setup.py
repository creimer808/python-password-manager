import sqlite3

conn = sqlite3.connect('passwords_database')
cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS passwords (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_email TEXT,
                   title TEXT
                   username TEXT
                   password TEXT
                   notes TEXT
               )
               ''')
conn.commit()
conn.close()