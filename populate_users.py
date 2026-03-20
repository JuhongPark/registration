"""
Populate Users Module (Q7)

Uses the Faker package to generate and insert 1,000 synthetic
users into the database.
"""

import hashlib
import mysql.connector
from faker import Faker
from db_connection import connect_to_database_with_db


def hash_password(password):
    """Securely hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def populate_users(count=1000):
    """
    Generate and insert synthetic users into the users table.
    Uses Faker to create realistic fake data for each field.
    Inserts in batches for better performance.
    """
    fake = Faker()
    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO users (username, email, password, city, company, job_title)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Build a list of tuples, each representing one synthetic user record
    batch = []
    for i in range(count):
        # Append index to username and email to guarantee uniqueness across runs
        username = f"{fake.user_name()}_{i}"
        email = f"{i}_{fake.email()}"
        # Hash each generated password before storing, same as manual user creation
        password = hash_password(fake.password())
        city = fake.city()
        company = fake.company()
        job_title = fake.job()
        batch.append((username, email, password, city, company, job_title))

    # Use executemany() to insert all records in one operation for efficiency
    try:
        cursor.executemany(insert_query, batch)
        connection.commit()
        print(f"Successfully inserted {cursor.rowcount} synthetic users.")
    except mysql.connector.Error as e:
        print(f"Error populating users: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


# Run population when executed directly
if __name__ == "__main__":
    populate_users()
