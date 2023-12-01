from database import db_operations
from encryption import password_hashing

def register_user(username, password):
    
    salt = password_hashing.generate_salt()
    
    hashed_password = password_hashing.hash_password(salt, password)
    print(salt)
    print(username)
    print(hashed_password)
    confirmation = db_operations.create_user(username, hashed_password, salt)
    
    return confirmation
    
def login_user(username,password):
    user_data = db_operations.login_user(username)
    
    if user_data:
        hashed_password = user_data[1]
        salt = user_data[2]
        
        input_password_hashed = password_hashing.hash_password(password,salt)
        
        if input_password_hashed == hashed_password:
            print("Login Successful!")
            return(user_id)
        else:
            print("Incorrect Password.")
            return(NULL)
        
    else:
        print("User not found")


    
    
