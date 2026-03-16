# Command-Line User Registration System

A Python + MySQL command-line application for managing user registrations. Create, search, update, and delete users through an interactive menu powered by [Rich](https://github.com/Textualize/rich), with support for bulk synthetic data generation via [Faker](https://github.com/joke2k/faker).

> Problem set description: [Google Docs Link](https://docs.google.com/document/d/1C0-vkygpJDE6BVTqVqehhI7Fgm3uyMytcfL9qjH7Qec/edit?usp=sharing)

## Quick Start

**Prerequisites:** Python 3.10+, Docker

```bash
# 1. Clone and enter the project
git clone <repository-url>
cd registration

# 2. Set up Python environment
python3 -m venv venv
source venv/bin/activate
pip install mysql-connector-python PyYAML faker rich

# 3. Start MySQL (wait ~30s for initialization)
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:latest

# 4. Run the application
python main.py
```

The app automatically creates the database and table on first run.

> **Note:** If your MySQL credentials differ from the defaults (`root`/`root`/`3306`), edit `db.yaml` before running.

## Features

| Feature | Description |
|---------|-------------|
| **User Registration** | Create users with username, email, hashed password, city, company, and job title |
| **User Lookup** | Search and display a single user by username |
| **User List** | View all registered users in a formatted table |
| **User Update** | Update a user's email or password (with re-hashing) |
| **User Deletion** | Remove a user by username with existence validation |
| **Bulk Population** | Generate 1,000 realistic synthetic users with Faker |
| **Interactive Menu** | Rich-powered CLI menu with input validation |

## Project Structure

```
registration/
├── db.yaml                      # MySQL connection credentials
├── db_connection.py             # DB connection (Q1)
├── create_database_and_table.py # DB and table setup (Q2)
├── create_user.py               # User creation (Q3)
├── read_users.py                # User retrieval and display (Q4)
├── update_user.py               # User update (Q5)
├── delete_user.py               # User deletion (Q6)
├── populate_users.py            # Synthetic data generation (Q7)
├── cli_menu.py                  # Interactive CLI menu (Q8)
└── main.py                      # Entry point integrating all modules (Q9)
```

## What Was Added Beyond the Base Requirements

- **Password hashing** — All passwords are stored as SHA-256 hashes, never in plain text
- **Input validation** — Empty fields, invalid emails, and duplicate usernames/emails are caught with clear error messages
- **Rich table output** — User listings use `rich.Table` for clean, readable formatting
- **Robust error handling** — Specific MySQL exceptions (e.g., `IntegrityError`) produce user-friendly messages instead of raw tracebacks
- **Batch insert** — `populate_users.py` uses `executemany()` for efficient bulk insertion
