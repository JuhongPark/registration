"""
Read Users Module (Q4)

Queries the users table and displays results in a clear
and formatted manner on the command line.
"""

from db_connection import connect_to_database_with_db


def read_all_users():
    """Retrieve and display all user records from the users table."""
    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT id, username, email, city, company, job_title FROM users")
        rows = cursor.fetchall()

        if not rows:
            print("No users found in the database.")
            return []

        # Display results in formatted columns
        print(f"\n{'ID':<5} {'Username':<20} {'Email':<30} {'City':<15} {'Company':<20} {'Job Title':<20}")
        print("-" * 110)

        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<30} {row[3]:<15} {row[4]:<20} {row[5]:<20}")

        print(f"\nTotal users: {len(rows)}")
        return rows

    except Exception as e:
        print(f"Error reading users: {e}")
        return []
    finally:
        cursor.close()
        connection.close()


def read_one_user(username):
    """Retrieve and display a single user record by username."""
    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "SELECT id, username, email, city, company, job_title FROM users WHERE username = %s",
            (username,)
        )
        row = cursor.fetchone()

        if not row:
            print(f"User '{username}' not found.")
            return None

        # Display the user record in a readable format
        print(f"\n--- User Details ---")
        print(f"ID:        {row[0]}")
        print(f"Username:  {row[1]}")
        print(f"Email:     {row[2]}")
        print(f"City:      {row[3]}")
        print(f"Company:   {row[4]}")
        print(f"Job Title: {row[5]}")
        return row

    except Exception as e:
        print(f"Error reading user: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Run read all users when executed directly
if __name__ == "__main__":
    read_all_users()
