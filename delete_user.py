"""
Delete User Module (Q6)

Removes a user from the database based on their username.
Handles cases where the specified user does not exist.
"""

import mysql.connector
from db_connection import connect_to_database_with_db


def delete_user():
    """
    Accept a username as input, delete the corresponding record
    from the users table, and handle non-existent users.
    """
    print("\n--- Delete User ---")
    username = input("Enter the username to delete: ")

    if not username.strip():
        print("Username cannot be empty.")
        return

    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM users WHERE username = %s", (username,))
        connection.commit()

        # Handle cases where the user does not exist
        if cursor.rowcount == 0:
            print(f"User '{username}' not found. No records deleted.")
        else:
            print(f"User '{username}' has been deleted successfully.")

    except mysql.connector.Error as e:
        print(f"Database error while deleting user: {e}")
    finally:
        cursor.close()
        connection.close()


# Run delete when executed directly
if __name__ == "__main__":
    delete_user()
