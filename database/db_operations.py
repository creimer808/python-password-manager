import sqlite3

###########################################################
##### Stuff to do with password database modification #####
###########################################################
def add_secrets_entry(user_email, title, username, password, notes):
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

def get_user_by_username(username):
    conn = sqlite3.connect('secrets.db')
    cursor = conn.cursor()

    cursor.execute()

### add an update password entry

    
    

    