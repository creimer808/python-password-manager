# Import necessary modules
from encryption import password_hashing
from database import db_operations

# Retrieve user data from the database
user_data = db_operations.get_user_by_email("john.doe@example.com")

if user_data:
    # Assuming the plain-text password is "user_password_here"
    password = "Password1!"

    # Generate a salt and hash the password
    salt = password_hashing.generate_salt()
    hashed_password = password_hashing.hash_password(password, salt)

    # Update the user's record in the database
    db_operations.update_user_password_and_salt("john.doe@example.com", hashed_password, salt)
