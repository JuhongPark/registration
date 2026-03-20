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


def read_all_users(page_size=20):
    """Retrieve and display all user records with pagination."""
    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    try:
        # Query all user records, excluding password hash from display
        cursor.execute("SELECT id, username, email, city, company, job_title FROM users")
        rows = cursor.fetchall()

        if not rows:
            console.print("No users found in the database.")
            return []

        total = len(rows)
        # Calculate total number of pages
        total_pages = (total + page_size - 1) // page_size
        page = 0

        while page < total_pages:
            # Slice the current page of rows
            start = page * page_size
            end = min(start + page_size, total)
            page_rows = rows[start:end]

            # Build a rich Table with styled columns for clear, formatted output
            table = Table(title=f"All Users (Page {page + 1}/{total_pages})")
            table.add_column("ID", style="cyan")
            table.add_column("Username", style="green")
            table.add_column("Email", style="yellow")
            table.add_column("City")
            table.add_column("Company")
            table.add_column("Job Title")

            # Populate each row, converting id from int to str for display
            for row in page_rows:
                table.add_row(str(row[0]), row[1], row[2], row[3], row[4], row[5])

            console.print(table)
            console.print(f"Showing {start + 1}-{end} of {total} users")

            # If there are more pages, prompt the user to continue or quit
            if page < total_pages - 1:
                nav = input("\nPress Enter for next page, or 'q' to quit: ").strip().lower()
                if nav == "q":
                    break
            page += 1

        return rows

    except mysql.connector.Error as e:
        print(f"Database error while reading users: {e}")
        return []
    finally:
        cursor.close()
        connection.close()


def read_one_user(username):
    """Retrieve and display user records by username, supporting partial match with LIKE."""
    connection = connect_to_database_with_db()
    cursor = connection.cursor()

    try:
        # Use LIKE with wildcards to allow partial username matching
        cursor.execute(
            "SELECT id, username, email, city, company, job_title FROM users WHERE username LIKE %s",
            (f"%{username}%",)
        )
        rows = cursor.fetchall()

        # Handle case where no matching user is found
        if not rows:
            console.print(f"No users matching '{username}' found.")
            return None

        # If exactly one match, display as a detailed panel
        if len(rows) == 1:
            row = rows[0]
            details = (
                f"[cyan]ID:[/cyan]        {row[0]}\n"
                f"[green]Username:[/green]  {row[1]}\n"
                f"[yellow]Email:[/yellow]     {row[2]}\n"
                f"City:      {row[3]}\n"
                f"Company:   {row[4]}\n"
                f"Job Title: {row[5]}"
            )
            console.print(Panel(details, title="User Details", border_style="cyan"))
            return rows[0]

        # If multiple matches, display all in a table
        console.print(f"Found {len(rows)} users matching '{username}':")
        table = Table(title="Search Results")
        table.add_column("ID", style="cyan")
        table.add_column("Username", style="green")
        table.add_column("Email", style="yellow")
        table.add_column("City")
        table.add_column("Company")
        table.add_column("Job Title")

        for row in rows:
            table.add_row(str(row[0]), row[1], row[2], row[3], row[4], row[5])

        console.print(table)
        return rows

    except mysql.connector.Error as e:
        print(f"Database error while reading user: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Run read all users when executed directly
if __name__ == "__main__":
    read_all_users()
