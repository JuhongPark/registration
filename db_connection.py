"""
Database Connection Module (Q1)

Establishes a connection to the MySQL database by loading
credentials from db.yaml using PyYAML.
"""

import os
import sys
import yaml
import mysql.connector


def get_db_config():
    """
    Load database credentials from the db.yaml configuration file.
    Looks for db.yaml in the same directory as this script.
    """
    # Resolve db.yaml path relative to this script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "db.yaml")

    try:
        # Read and parse the YAML configuration file using safe_load
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file not found at '{config_path}'.")
        print("Please create a db.yaml file with your MySQL credentials.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse db.yaml — {e}")
        sys.exit(1)

    # Return only the 'mysql' section containing host, user, password, port
    return config["mysql"]


def connect_to_database(verbose=True):
    """
    Connect to the MySQL server using credentials from db.yaml.
    Returns the connection object. Displays a confirmation message
    when verbose is True (default for standalone use).
    """
    config = get_db_config()

    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            port=config["port"]
        )
    except mysql.connector.Error as e:
        print(f"Error: Could not connect to MySQL server — {e}")
        sys.exit(1)

    # Display confirmation message once connected
    if verbose:
        print("Successfully connected to the MySQL database.")
    return connection


def connect_to_database_with_db(database="users_db", verbose=False):
    """
    Connect to a specific MySQL database.
    Used by CRUD modules that need direct access to users_db.
    Verbose is False by default to keep CRUD output clean.
    """
    config = get_db_config()

    try:
        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            port=config["port"],
            database=database
        )
    except mysql.connector.Error as e:
        print(f"Error: Could not connect to '{database}' — {e}")
        sys.exit(1)

    if verbose:
        print(f"Successfully connected to the '{database}' database.")
    return connection


# Run connection test when executed directly — displays confirmation per Q1 spec
if __name__ == "__main__":
    conn = connect_to_database()
    conn.close()
    print("Connection closed.")
