from database import db_operations
from encryption import password_hashing

def register_user(username, password):
    
    salt = password_hashing.generate_salt()
    
    hashed_password = password_hashing.hash_password(salt, password)
    confirmation = db_operations.create_user(username, hashed_password, salt)
    
    return confirmation
    
def login_user(username,login_password):
    user_data = db_operations.login_user(username)
    
    if user_data is not None:
        hashed_password = user_data[2]
        salt = user_data[3]
        
        input_password_hashed = password_hashing.hash_password(login_password,salt)
        
        if input_password_hashed == hashed_password:
            print("Login Successful!")
            return(user_data[0])
        else:
            print("Incorrect Password.")
            return(-1)
        
    else:
        print("User not found")


    
    
