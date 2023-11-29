import sqlite3

def add_user(first_name, last_name, email, hashed_password,salt):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    
    cursor.execute(''' 
                   INSERT INTO users (first_name, last_name, email, hashed_password, salt)
                   VALUES (?, ?, ?, ?, ?)
                   ''',(first_name, last_name, email, hashed_password, salt))
    
    conn.commit()
    conn.close()

def get_user_by_email():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE EMAIL =?', (email,))
    user_data = cursor.fetchone()
    
    conn.close()
    
    return user_data

    