import sqlite3

###########################################################
####################### User Data  ########################
###########################################################
def create_user(username, hashed_password, salt):
    conn = sqlite3.connect('secrets.db')
    cursor = conn.cursor()
    
    cursor.execute('Select * FROM users WHERE username = ?', (username,)) 
    existing_user = cursor.fetchone()
    
    if existing_user:
        return(0)
    else:
        cursor.execute('''
                    INSERT INTO users (username, hashed_password, salt)
                    VALUES (?, ?, ?)
                    ''', (username, hashed_password, salt))
        conn.commit()
        conn.close()
        return(1)
    
    conn.commit()
    conn.close()

    
def login_user(username, password):
    conn = sqlite3.connect('secrets.db')
    cursor = conn.cursor()
    
    cursor.execute(''' 
                    SELECT from users WHERE username = ?
                    ''', (username))
    
    conn.commit()
    conn.close()
    
    


###########################################################
##### Stuff to do with password database modification #####
###########################################################
def add_secrets_entry(title, username, password, notes):
    conn = sqlite3.connect('secrets.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO passwords (title, username, password, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_email, title, username, password, notes))

    conn.commit()
    conn.close()

def get_secrets_entries_for_user(user_id):
    conn = sqlite3.connect('secrets.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM passwords WHERE user_email = ?', (user_id,))
    password_entries = cursor.fetchall()

    conn.close()

    return password_entries


### add an update password entry

    
    

    