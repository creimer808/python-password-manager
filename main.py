# main.py
from authentication import authentication
from secrets import secrets_operations

def main():
    print("Welcome to the Secrets Manager!")

    while True:
        print("Menu:")
        print("1. Login")
        print("2. Create a New User")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            login_username = input("Enter Username: ")
            login_password = input("Enter Password: ")
            user_id = authentication.login_user(login_username, login_password)

            if user_id is not None:
                while True:
                    print("Menu:")
                    print("1. List All Secrets")
                    print("2. Open Secret")
                    print("3. Add Secret")
                    print("4. Exit")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        secrets = secrets_operations.list_all_secrets(user_id)
                        print("All Secrets:")
                        for secret in secrets:
                            print(f"ID: {secret[0]}, Username: {secret[2]}, Password: {secret[3]}, Notes: {secret[4]}")
                        print()

                    elif choice == '2':
                        secret_id = input("Enter the ID of the secret you want to open: ")
                        secret = secrets_operations.open_secret(secret_id)
                        if secret:
                            print(f"\nSecret Details:")
                            print(f"Username: {secret[2]}, Password: {secret[3]}, Notes: {secret[4]}\n")
                        else:
                            print("Secret not found.\n")

                    elif choice == '3':
                        username = input("Enter the username: ")
                        password = input("Enter the password: ")
                        notes = input("Enter any notes: ")
                        secrets_operations.add_secret(user_id, username, password, notes)
                        print("Secret added successfully!\n")

                    elif choice == '4':
                        print("Exiting Secrets Manager. Goodbye!")
                        break

                    else:
                        print("Invalid choice. Please enter a valid option.\n")
            else:
                print("Login failed. Please try again.\n")

        elif choice == '2':
            new_username = input("Enter Your Username: ")
            new_password = input("Enter Your Password: ")
            authentication.register_user(new_username, new_password)
            print("User created successfully! Please Login.\n")

        elif choice == '3':
            print("Exiting Secrets Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
