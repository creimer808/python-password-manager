class User:
    def __init__(self, first_name, last_name, email, hashed_password, salt):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hashed_password = hashed_password
        self.salt = salt
        
class PasswordEntry:
    def __init__(self,user_email,title,username,password,notes):
        self.user_email = user_email
        self.title = title
        self.username = username
        self.password = password
        self.notes = notes