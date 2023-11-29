import sqlite3

def list_columns(users):
    # Connect to the database
    connection = sqlite3.connect('user_database.db')

    # Create a cursor
    cursor = connection.cursor()

    try:
        # Execute an SQL query to fetch column names
        cursor.execute(f"PRAGMA table_info({users})")
        
        # Fetch all rows
        columns_info = cursor.fetchall()

        # Extract column names from the result
        column_names = [column[1] for column in columns_info]

        # Print the column names
        print(f"Columns in '{users}': {', '.join(column_names)}")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        connection.close()

# Replace 'your_database.db' and 'your_table' with your actual database file name and table name
list_columns('users')
