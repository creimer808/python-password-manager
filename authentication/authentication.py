from database import db_operations

def register_user(first_name, last_name, email, hashed_password, salt):
    db_operations.add_user(first_name, last_name, email, hashed_password, salt)