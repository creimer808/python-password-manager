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

def get_user_by_email(email):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users WHERE EMAIL = ?', (email,))
    user_data = cursor.fetchone()
    
    conn.close()
    
    return user_data

def update_user_password_and_salt():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
                   UPDATE users
                   SET hashed_password = ?, salt = ?
                   WHERE email = ?
                   ''', (hash_password, salt, email))
    
    conn.commit
    conn.close
    
    
    

    