"""
Main Entry Point (Q9)

Integrates all previously implemented functionalities into a single
executable script. Coordinates interactions between modules and
ensures proper error handling across the application.
"""

from create_database_and_table import setup_database
from populate_users import populate_users  # noqa: F401 — imported for integration
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
