# Problem Set

## Command-Line User Registration System

### Objective

The goal of this assignment is to build a simple command-line user registration system using Python and MySQL. You will gain hands-on experience connecting to a database, executing SQL CRUD operations (Create, Read, Update, Delete), generating synthetic data, and designing a user-friendly command-line interface. This assignment reinforces the concepts discussed in our lectures on Containers & Databases and problem-based learning approaches.

### Requirements

- **Programming Language:** Python
- **Database:** MySQL (to be run within a Docker container via GitHub CodeSpaces)
- **Tools & Libraries:**
  - GitHub CodeSpaces (using the default blank template)
  - Docker (for running a MySQL container)
  - Python packages:
    - `mysql-connector-python` (for database connectivity)
    - `PyYAML` (to read connection credentials from a YAML file)
    - `Faker` (to generate synthetic user data)
    - `rich` (for an enhanced command-line UI using panels)
- **Files to Create:**
  - `db.yaml`
  - `db_connection.py`
  - `create_database_and_table.py`
  - `create_user.py`
  - `read_users.py`
  - `update_user.py`
  - `delete_user.py`
  - `populate_users.py`
  - `cli_menu.py`
  - `main.py`

### Assignment Description

Your application will manage user registration using a single MySQL database that contains one table named **users**. The system must support all CRUD operations and provide a menu-driven interface for user interaction. Complete the following questions:

### Question 1: Database Connection (db_connection.py)

**Description:**
Write Python code to establish a connection to the MySQL database.

- **Task:**
  - Load the database credentials (host, user, password, port) from a `db.yaml` file.
  - Connect to the MySQL server and display a confirmation message once the connection is successfully established.

### Question 2: Creating the Database and Table (create_database_and_table.py)

**Description:**
Create the database and the table required for the assignment.

- **Task:**
  - Write Python code to create a database (e.g., `users_db`) if it does not already exist.
  - Create a table named **users** with the following fields:
    - `id`: A unique identifier (Primary Key, Auto-Incremented)
    - `username`: The user's chosen username (Unique, Required)
    - `email`: The user's email address (Unique, Required)
    - `password`: The user's password
    - `city`: The city where the user is located
    - `company`: The name of the company the user is associated with
    - `job_title`: The user's job title representing their role in the company

### Question 3: Creating Users (create_user.py)

**Description:**
Write Python code to insert a new user into the **users** table.

- **Task:**
  - Accept input for username, email, password, city, company, and job title.
  - Validate the inputs and securely hash the password before storing it.
  - Insert the new user record into the database.

### Question 4: Reading Users (read_users.py)

**Description:**
Write Python code to retrieve and display all user records from the database.

- **Task:**
  - Query the **users** table.
  - Display the results in a clear and formatted manner on the command line.

### Question 5: Updating User Information (update_user.py)

**Description:**
Write Python code to update an existing user's email or password.

- **Task:**
  - Allow the user to specify which field (email or password) to update.
  - Validate and perform the update, then confirm the change to the user.

### Question 6: Deleting a User (delete_user.py)

**Description:**
Write Python code to remove a user from the database based on their username.

- **Task:**
  - Accept the username as input.
  - Delete the corresponding record from the **users** table.
  - Handle cases where the specified user does not exist.

### Question 7: Populating the Database (populate_users.py)

**Description:**
Utilize the Faker package to generate synthetic user data.

- **Task:**
  - Generate and insert 1,000 synthetic users

### Question 8: Command-Line Interface (cli_menu.py)

**Description:**
Develop a command-line menu using the `rich` library (e.g., `rich.panel`) for enhanced UI.

- **Task:**
  - Implement a menu that offers options to:
    - Create a new user
    - Read/display one user
    - Read/display all users
    - Update an existing user
    - Delete a user
    - Exit the application
  - Ensure the interface handles user inputs gracefully and routes them to the correct operations.

### Question 9: Integrating All Functionalities (main.py)

**Description:**
Integrate all previously implemented functionalities into a single executable script.

- **Task:**
  - Use `main.py` as the entry point to coordinate interactions between the modules.
  - Ensure smooth integration and proper error handling across the application.

### Additional Guidelines

- **Documentation:**
  - Comment your code thoroughly to explain your logic and key sections.

## Source

Original document: [Google Docs Link](https://docs.google.com/document/d/1C0-vkygpJDE6BVTqVqehhI7Fgm3uyMytcfL9qjH7Qec/edit?usp=sharing)
