import sqlite3

###########################################################
####### Stuff to do with users database modification ######
###########################################################
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

###########################################################
##### Stuff to do with password database modification #####
###########################################################
def add_password_entry(user_email, title, username, password, notes):
    conn = sqlite3.connect('passwords_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO passwords (user_email, title, username, password, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_email, title, username, password, notes))

    conn.commit()
    conn.close()

def get_password_entries_for_user(user_email):
    conn = sqlite3.connect('passwords_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM passwords WHERE user_email = ?', (user_email,))
    password_entries = cursor.fetchall()

    conn.close()

    return password_entries

### add an update password entry

    
    

    