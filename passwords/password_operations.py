from database import db_operations
def add_password_entry(user_email, title, username, password, notes):
        db_operations.add_password_entry (user_email, title, username, password, notes)
        
def get_password_entry_for_user(user_email):
    return db_operations.get_password_enteries_for_user(user_email)