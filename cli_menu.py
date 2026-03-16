"""
Command-Line Interface Module (Q8)

Develops a command-line menu using the rich library for enhanced UI.
Provides options to create, read, update, delete users, and exit.
"""

from rich.console import Console
from rich.panel import Panel

from create_user import create_user
from read_users import read_all_users, read_one_user
from update_user import update_user
from delete_user import delete_user

# Initialize rich console for enhanced output
console = Console()


def display_menu():
    """Display the main menu using rich panel for enhanced UI."""
    menu_text = (
        "[bold cyan]1.[/bold cyan] Create a new user\n"
        "[bold cyan]2.[/bold cyan] Read/display one user\n"
        "[bold cyan]3.[/bold cyan] Read/display all users\n"
        "[bold cyan]4.[/bold cyan] Update an existing user\n"
        "[bold cyan]5.[/bold cyan] Delete a user\n"
        "[bold cyan]6.[/bold cyan] Exit"
    )
    console.print(Panel(menu_text, title="User Registration System", border_style="cyan"))


def run_menu():
    """
    Run the main menu loop. Handles user input and routes
    to the correct operation based on the selected option.
    """
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            # Create a new user
            create_user()

        elif choice == "2":
            # Read/display one user by username
            username = input("Enter the username to search: ")
            read_one_user(username)

        elif choice == "3":
            # Read/display all users
            read_all_users()

        elif choice == "4":
            # Update an existing user
            update_user()

        elif choice == "5":
            # Delete a user
            delete_user()

        elif choice == "6":
            # Exit the application
            console.print("[bold green]Goodbye![/bold green]")
            break

        else:
            # Handle invalid input gracefully
            console.print("[bold red]Invalid choice. Please enter a number between 1 and 6.[/bold red]")


# Run the menu when executed directly
if __name__ == "__main__":
    run_menu()
