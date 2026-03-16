"""
Database Connection Module (Q1)

Establishes a connection to the MySQL database by loading
credentials from db.yaml using PyYAML.
"""

import yaml
import mysql.connector


def get_db_config():
    """Load database credentials from the db.yaml configuration file."""
    with open("db.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config["mysql"]


def connect_to_database():
    """
    Connect to the MySQL server using credentials from db.yaml.
    Returns the connection object and displays a confirmation message.
    """
    config = get_db_config()

    # Establish connection to MySQL server
    connection = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        port=config["port"]
    )

    # Display confirmation message once connected
    print("Successfully connected to the MySQL database.")
    return connection


def connect_to_database_with_db(database="users_db"):
    """
    Connect to a specific MySQL database.
    Used by CRUD modules that need direct access to users_db.
    """
    config = get_db_config()

    connection = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        port=config["port"],
        database=database
    )

    print(f"Successfully connected to the '{database}' database.")
    return connection


# Run connection test when executed directly
if __name__ == "__main__":
    conn = connect_to_database()
    conn.close()
    print("Connection closed.")
