from passwords import password_operations
from getpass import getpass

def run_password_manager(user_email):
    while True:
        print("Password Manager Menu:")
        print("1. Add Password Entry")
        print("2. View Password Entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            username = input("Enter username: ")
            password = getpass("Enter password (hidden): ")
            notes = input("Enter notes: ")

            password_operations.add_password_entry(user_email, title, username, password, notes)
            print("Password entry added successfully!\n")

        elif choice == '2':
            password_entries = password_operations.get_password_entries_for_user(user_email)
            if password_entries:
                print("\nPassword Entries:")
                for entry in password_entries:
                    print(f"Title: {entry[2]}, Username: {entry[3]}, Password: {entry[4]}, Notes: {entry[5]}")
                print()
            else:
                print("No password entries found.\n")

        elif choice == '3':
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.\n")
