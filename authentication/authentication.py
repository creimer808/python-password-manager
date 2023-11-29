from database import db_operations
from encryption import password_hashing

def register_user(username, hashed_password, salt):
    db_operations.add_user(username, hashed_password, salt)
    
def login_user(username,password):
    user_data = db_operations.get_user_by_username(username)
    
    if user_data:
        hashed_password = user_data[4]
        salt = user_data[5]
        
        input_password_hashed = password_hashing.hash_password(password,salt)
        
        if input_password_hashed == hashed_password:
            print("Login Successful!")
        else:
            print("Incorrect Password.")
        
    else:
        print("User not found")


    
