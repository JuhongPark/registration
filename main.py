"""
Main Entry Point (Q9)

Integrates all previously implemented functionalities into a single
executable script. Coordinates interactions between modules and
ensures proper error handling across the application.
"""

import sys
from create_database_and_table import setup_database
from populate_users import populate_users
from cli_menu import run_menu


def main():
    """
    Application entry point. Sets up the database and table,
    then launches the interactive CLI menu.
    """
    try:
        # Initialize the database and table before starting the menu
        print("Initializing database...")
        setup_database()
        print()

        # Allow populating the database via command-line argument
        if len(sys.argv) > 1 and sys.argv[1] == "--populate":
            print("Populating database with synthetic users...")
            populate_users()
            print()

        # Launch the interactive CLI menu
        run_menu()

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nApplication interrupted. Exiting...")
    except Exception as e:
        # Catch any unexpected errors at the top level
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
