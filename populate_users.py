"""
Populate Users Module (Q7)

Uses the Faker package to generate and insert 1,000 synthetic
users into the database.
"""

import hashlib
from faker import Faker
from db_connection import connect_to_database_with_db


def hash_password(password):
    """Securely hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def populate_users(count=1000):
    """
    Generate and insert synthetic users into the users table.
    Uses Faker to create realistic fake data for each field.
    """
    fake = Faker()
    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO users (username, email, password, city, company, job_title)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Track how many users were successfully inserted
    inserted = 0

    for i in range(count):
        try:
            # Generate unique username by appending index to avoid duplicates
            username = f"{fake.user_name()}_{i}"
            email = f"{i}_{fake.email()}"
            password = hash_password(fake.password())
            city = fake.city()
            company = fake.company()
            job_title = fake.job()

            cursor.execute(insert_query, (username, email, password, city, company, job_title))
            inserted += 1

        except Exception as e:
            # Skip duplicates or other errors and continue
            print(f"Skipped user {i}: {e}")

    # Commit all inserted records at once
    connection.commit()
    cursor.close()
    connection.close()

    print(f"Successfully inserted {inserted} out of {count} synthetic users.")


# Run population when executed directly
if __name__ == "__main__":
    populate_users()
