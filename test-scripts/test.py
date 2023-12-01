import sqlite3
def main():
    list_columns()
#first_name = "John"
#last_name = "Doe"
#email = "john.doe@example.com"
#hashed_password = "Password1!"
#salt="test-salt"

#register user:
#authentication.register_user(first_name, last_name, email, hashed_password, salt)

#email = "john.doe@example.com"
#password = "Password1!"

#authentication.login_user(email,password)

### Connect to DB, list all columns in USERS table. ###
def list_columns():    
    conn = sqlite3.connect('secrets.db')
    cursor = conn.cursor()
        
    cursor.execute("PRAGMA table_info(users)")
    columns = cursor.fetchall()

    for i in columns:
        print(columns[1])

    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    main()