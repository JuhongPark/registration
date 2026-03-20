"""
Create User Module (Q3)

Accepts input for user details, validates inputs,
securely hashes the password, and inserts the new user into the database.
"""

import hashlib
import mysql.connector
from db_connection import connect_to_database_with_db


def hash_password(password):
    """Securely hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def validate_inputs(username, email, password):
    """
    Validate that required fields are not empty and email contains '@'.
    Returns a tuple (is_valid, error_message).
    """
    if not username.strip():
        return False, "Username cannot be empty."
    if not email.strip() or "@" not in email:
        return False, "A valid email address is required."
    if not password.strip():
        return False, "Password cannot be empty."
    return True, ""


def create_user():
    """
    Prompt the user for registration details, validate inputs,
    hash the password, and insert the record into the users table.
    """
    # Accept input for all user fields
    print("\n--- Create New User ---")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    city = input("Enter city: ")
    company = input("Enter company: ")
    job_title = input("Enter job title: ")

    # Validate required inputs
    is_valid, error_msg = validate_inputs(username, email, password)
    if not is_valid:
        print(f"Validation error: {error_msg}")
        return

    # Securely hash the password before storing
    hashed_password = hash_password(password)

    # Connect to users_db and insert the new user record
    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    try:
        # Use parameterized query to safely insert user data and prevent SQL injection
        insert_query = """
        INSERT INTO users (username, email, password, city, company, job_title)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (username, email, hashed_password, city, company, job_title))
        connection.commit()
        print(f"User '{username}' created successfully.")
    except mysql.connector.IntegrityError:
        # Handle duplicate username or email
        print(f"Error: Username '{username}' or email '{email}' already exists.")
    except mysql.connector.Error as e:
        print(f"Database error while creating user: {e}")
    finally:
        cursor.close()
        connection.close()


# Run user creation when executed directly
if __name__ == "__main__":
    create_user()
