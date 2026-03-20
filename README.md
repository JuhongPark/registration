# Command-Line User Registration System

A Python + MySQL command-line application for managing user registrations. Supports full CRUD operations (Create, Read, Update, Delete), synthetic data generation, and a menu-driven interface with an enhanced UI.

> Problem set description: [Google Docs Link](https://docs.google.com/document/d/1C0-vkygpJDE6BVTqVqehhI7Fgm3uyMytcfL9qjH7Qec/edit?usp=sharing)

## Requirements

- **Programming Language:** Python 3.10+
- **Database:** MySQL (running in a Docker container)
- **Python Packages:**
  - `mysql-connector-python` — Database connectivity
  - `PyYAML` — Reading connection credentials from a YAML file
  - `Faker` — Generating synthetic user data
  - `rich` — Enhanced command-line UI using panels and tables

## Quick Start

```bash
# 1. Clone and enter the project
git clone <repository-url>
cd registration

# 2. Set up Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Start MySQL (wait ~30s for first-time initialization)
# First time:
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:latest
# Already created before? Just restart it:
docker start mysql-container

# 4. Run the application
python main.py
```

The app automatically creates the database and table on first run.

> **Note:** If your MySQL credentials differ from the defaults (`root`/`root`/`3306`), edit `db.yaml` before running.

## Project Structure

```
registration/
├── db.yaml                      # MySQL connection credentials
├── db_connection.py             # Database connection (Q1)
├── create_database_and_table.py # Database and table creation (Q2)
├── create_user.py               # User creation with validation and hashing (Q3)
├── read_users.py                # User retrieval and formatted display (Q4)
├── update_user.py               # User email/password update (Q5)
├── delete_user.py               # User deletion with existence check (Q6)
├── populate_users.py            # Synthetic data generation with Faker (Q7)
├── cli_menu.py                  # Interactive CLI menu using rich (Q8)
└── main.py                      # Entry point integrating all modules (Q9)
```

## Implementation Details (Q1–Q9)

### Q1: Database Connection (`db_connection.py`)
Loads database credentials (host, user, password, port) from `db.yaml` using PyYAML. Connects to the MySQL server and displays a confirmation message on success.

### Q2: Creating the Database and Table (`create_database_and_table.py`)
Creates the `users_db` database if it does not already exist, then creates the `users` table with the following fields:
- `id` — Primary Key, Auto-Incremented
- `username` — Unique, Required
- `email` — Unique, Required
- `password` — Stores the hashed password
- `city` — User's city
- `company` — User's company name
- `job_title` — User's job title

### Q3: Creating Users (`create_user.py`)
Accepts input for username, email, password, city, company, and job title. Validates inputs (empty fields, email format) and securely hashes the password using SHA-256 before inserting into the database.

### Q4: Reading Users (`read_users.py`)
Queries the `users` table and displays results in a clear and formatted manner using `rich.Table`. Supports both viewing all users and looking up a single user.

### Q5: Updating User Information (`update_user.py`)
Allows the user to specify which field to update (email or password). Validates the new value, performs the update, and confirms the change.

### Q6: Deleting a User (`delete_user.py`)
Accepts a username as input, deletes the corresponding record from the `users` table, and handles cases where the specified user does not exist.

### Q7: Populating the Database (`populate_users.py`)
Uses the Faker package to generate and insert 1,000 synthetic users into the database. Uses `executemany()` for efficient batch insertion.

### Q8: Command-Line Interface (`cli_menu.py`)
A menu-driven interface built with `rich.Panel` that offers options to:
1. Create a new user
2. Read/display one user
3. Read/display all users
4. Update an existing user
5. Delete a user
6. Populate 1,000 synthetic users
7. Exit the application

Handles user inputs gracefully and routes them to the correct operations.

### Q9: Integrating All Functionalities (`main.py`)
Entry point that coordinates all modules. Runs database setup on startup, then launches the interactive CLI menu. Includes top-level error handling for smooth operation.

## What Was Added Beyond the Base Requirements

- **Password hashing** — All passwords are stored as SHA-256 hashes, never in plain text
- **Hidden password input** — Uses `getpass` to hide password characters during creation and update
- **Input validation** — Empty fields, invalid emails, and duplicate usernames/emails are caught with clear error messages
- **Delete confirmation** — Prompts "Are you sure?" before deleting a user to prevent accidental removal
- **Partial username search** — User lookup supports partial matching via SQL `LIKE`, showing a table when multiple users match
- **Pagination** — `read_all_users` displays results in pages of 20, with navigation to avoid overwhelming output
- **Rich table output** — User listings use `rich.Table` for clean, readable formatting
- **Robust error handling** — Specific MySQL exceptions (e.g., `IntegrityError`) produce user-friendly messages instead of raw tracebacks
- **Batch insert** — `populate_users.py` uses `executemany()` for efficient bulk insertion
