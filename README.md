# Command-Line User Registration System

A simple command-line user registration system using Python and MySQL. Supports full CRUD operations, synthetic data generation, and an interactive menu interface.

Problem set description document: [Document Link](https://docs.google.com/document/d/1C0-vkygpJDE6BVTqVqehhI7Fgm3uyMytcfL9qjH7Qec/edit?usp=sharing).

## Prerequisites

- Python 3.10+
- Docker (for running a MySQL container)

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd registration
```

### 2. Create a virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install mysql-connector-python PyYAML faker rich
```

### 3. Start a MySQL server using Docker

```bash
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:latest
```

Wait about 20–30 seconds for MySQL to finish initializing before proceeding.

### 4. Configure database credentials

Edit `db.yaml` if your MySQL credentials differ from the defaults:

```yaml
mysql:
  host: "localhost"
  user: "root"
  password: "root"
  port: 3306
```

## Usage

### Run the application

```bash
source venv/bin/activate
python main.py
```

This will automatically create the database and table, then launch the interactive menu.

### Run individual modules

Each module can also be executed independently:

```bash
python db_connection.py              # Test database connection
python create_database_and_table.py  # Set up database and table
python create_user.py                # Create a single user
python read_users.py                 # Display all users
python update_user.py                # Update a user's email or password
python delete_user.py                # Delete a user by username
python populate_users.py             # Populate 1,000 synthetic users
python cli_menu.py                   # Launch the interactive menu
```

## Project Structure

| File | Description |
|------|-------------|
| `db.yaml` | MySQL connection credentials |
| `db_connection.py` | Database connection module |
| `create_database_and_table.py` | Database and table creation |
| `create_user.py` | User creation with input validation and password hashing |
| `read_users.py` | User retrieval and formatted display |
| `update_user.py` | User email/password update |
| `delete_user.py` | User deletion with existence checking |
| `populate_users.py` | Synthetic user generation using Faker |
| `cli_menu.py` | Interactive CLI menu using Rich |
| `main.py` | Main entry point integrating all modules |

## Dependencies

| Package | Purpose |
|---------|---------|
| `mysql-connector-python` | MySQL database connectivity |
| `PyYAML` | Loading credentials from YAML config |
| `Faker` | Generating synthetic user data |
| `rich` | Enhanced command-line UI with panels |
