"""
Read Users Module (Q4)

Queries the users table and displays results in a clear
and formatted manner on the command line.
"""

import mysql.connector
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from db_connection import connect_to_database_with_db

# Initialize rich console for formatted output
console = Console()


def read_all_users():
    """Retrieve and display all user records from the users table."""
    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    try:
        # Query all user records, excluding password hash from display
        cursor.execute("SELECT id, username, email, city, company, job_title FROM users")
        rows = cursor.fetchall()

        if not rows:
            console.print("No users found in the database.")
            return []

        # Build a rich Table with styled columns for clear, formatted output
        table = Table(title="All Users")
        table.add_column("ID", style="cyan")
        table.add_column("Username", style="green")
        table.add_column("Email", style="yellow")
        table.add_column("City")
        table.add_column("Company")
        table.add_column("Job Title")

        # Populate each row, converting id from int to str for display
        for row in rows:
            table.add_row(str(row[0]), row[1], row[2], row[3], row[4], row[5])

        console.print(table)
        # Show total count below the table for quick reference
        console.print(f"\nTotal users: {len(rows)}")
        return rows

    except mysql.connector.Error as e:
        print(f"Database error while reading users: {e}")
        return []
    finally:
        cursor.close()
        connection.close()


def read_one_user(username):
    """Retrieve and display a single user record by username."""
    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    try:
        # Query a single user by username using parameterized query
        cursor.execute(
            "SELECT id, username, email, city, company, job_title FROM users WHERE username = %s",
            (username,)
        )
        row = cursor.fetchone()

        # Handle case where no matching user is found
        if not row:
            console.print(f"User '{username}' not found.")
            return None

        # Format the user record as a rich Panel for single-record display
        details = (
            f"[cyan]ID:[/cyan]        {row[0]}\n"
            f"[green]Username:[/green]  {row[1]}\n"
            f"[yellow]Email:[/yellow]     {row[2]}\n"
            f"City:      {row[3]}\n"
            f"Company:   {row[4]}\n"
            f"Job Title: {row[5]}"
        )
        console.print(Panel(details, title="User Details", border_style="cyan"))
        return row

    except mysql.connector.Error as e:
        print(f"Database error while reading user: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Run read all users when executed directly
if __name__ == "__main__":
    read_all_users()
