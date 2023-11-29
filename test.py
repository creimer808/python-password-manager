from authentication import authentication

#first_name = "John"
#last_name = "Doe"
#email = "john.doe@example.com"
#hashed_password = "Password1!"
#salt="test-salt"

#register user:
#authentication.register_user(first_name, last_name, email, hashed_password, salt)

email = "john.doe@example.com"
password = "Password1!"

authentication.login_user(email,password)

