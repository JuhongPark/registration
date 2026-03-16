"""
Update User Module (Q5)

Allows the user to update an existing user's email or password.
Validates the new value and confirms the change.
"""

import hashlib
import mysql.connector
from db_connection import connect_to_database_with_db


def hash_password(password):
    """Securely hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def update_user():
    """
    Prompt for a username and the field to update (email or password).
    Validate the new value, perform the update, and confirm the change.
    """
    print("\n--- Update User ---")
    username = input("Enter the username to update: ")

    # Let the user choose which field to update
    print("Which field would you like to update?")
    print("1. Email")
    print("2. Password")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        new_email = input("Enter the new email: ")
        # Validate email format
        if not new_email.strip() or "@" not in new_email:
            print("Invalid email address.")
            return
        field = "email"
        new_value = new_email

    elif choice == "2":
        new_password = input("Enter the new password: ")
        if not new_password.strip():
            print("Password cannot be empty.")
            return
        field = "password"
        # Hash the new password before storing
        new_value = hash_password(new_password)

    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    # Perform the update in the database
    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    try:
        # First check if the user exists
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
        if cursor.fetchone()[0] == 0:
            print(f"User '{username}' not found. No changes made.")
            return

        # Use whitelisted field names to prevent SQL injection
        allowed_fields = {"email", "password"}
        if field not in allowed_fields:
            print("Invalid field.")
            return
        update_query = f"UPDATE users SET {field} = %s WHERE username = %s"
        cursor.execute(update_query, (new_value, username))
        connection.commit()

        print(f"User '{username}' {field} updated successfully.")

    except mysql.connector.IntegrityError:
        # Handle duplicate email when updating
        print(f"Error: The email '{new_value}' is already in use by another user.")
    except mysql.connector.Error as e:
        print(f"Database error while updating user: {e}")
    finally:
        cursor.close()
        connection.close()


# Run update when executed directly
if __name__ == "__main__":
    update_user()
