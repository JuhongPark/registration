"""
Database and Table Creation Module (Q2)

Creates the 'users_db' database if it does not already exist,
then creates the 'users' table with the required fields.
"""

import mysql.connector
from db_connection import connect_to_database


def create_database(cursor):
    """Create the 'users_db' database if it does not already exist."""
    cursor.execute("CREATE DATABASE IF NOT EXISTS users_db")
    print("Database 'users_db' is ready.")


def create_users_table(cursor):
    """
    Create the 'users' table with the following fields:
    - id: Primary Key, Auto-Incremented
    - username: Unique, Required
    - email: Unique, Required
    - password: stores the hashed password
    - city: user's city
    - company: user's company name
    - job_title: user's job title
    """
    cursor.execute("USE users_db")

    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255),
        city VARCHAR(255),
        company VARCHAR(255),
        job_title VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)
    print("Table 'users' is ready.")


def setup_database():
    """Run the full database setup: create database and table."""
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        create_database(cursor)
        create_users_table(cursor)
        connection.commit()
        print("Database setup complete.")
    except mysql.connector.Error as e:
        print(f"Error during database setup: {e}")
    finally:
        cursor.close()
        connection.close()


# Run setup when executed directly
if __name__ == "__main__":
    setup_database()
