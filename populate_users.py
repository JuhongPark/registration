"""
Populate Users Module (Q7)

Uses the Faker package to generate and insert 1,000 synthetic
users into the database.

Usage:
    Run this script directly to populate the database:
        python populate_users.py
"""

import mysql.connector
from faker import Faker
from db_connection import connect_to_database_with_db
from create_user import hash_password  # Reuse hashing logic implemented in Q3


def populate_users(count=1000):
    """
    Generate and insert synthetic users into the users table.
    Uses Faker to create realistic fake data for each field.
    Inserts in batches for better performance.
    """
    fake = Faker()
    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    # Use INSERT IGNORE to skip duplicates gracefully on repeated runs
    insert_query = """
    INSERT IGNORE INTO users (username, email, password, city, company, job_title)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Build a list of tuples using fake.unique to generate distinct values
    batch = []
    for _ in range(count):
        username = fake.unique.user_name()
        email = fake.unique.email()
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
        inserted = cursor.rowcount
        skipped = count - inserted
        print(f"Successfully inserted {inserted} synthetic users.")
        if skipped > 0:
            print(f"Skipped {skipped} duplicates.")
    except mysql.connector.Error as e:
        print(f"Error populating users: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


# Run population when executed directly
if __name__ == "__main__":
    populate_users()
