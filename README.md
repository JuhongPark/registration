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

## Features

| Menu Option | Description |
|-------------|-------------|
| **Create a new user** | Register a user with username, email, password, city, company, and job title |
| **Read/display one user** | Search and display a user by username |
| **Read/display all users** | View all registered users in a formatted table |
| **Update an existing user** | Update a user's email or password |
| **Delete a user** | Remove a user by username |
| **Populate 1,000 users** | Generate synthetic users using Faker |

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

## Additional Enhancements

- **Hidden password input** — Uses `getpass` to hide password characters during creation and update
- **Delete confirmation** — Prompts "Are you sure?" before deleting a user to prevent accidental removal
- **Partial username search** — User lookup supports partial matching via SQL `LIKE`, showing a table when multiple users match
- **Pagination** — `read_all_users` displays results in pages of 20, with navigation to avoid overwhelming output
