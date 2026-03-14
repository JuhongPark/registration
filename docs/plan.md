# Project Plan: Command-Line User Registration System

## Persona Definitions

### Persona 1: DB Architect
**Responsible files:** `db.yaml`, `db_connection.py`, `create_database_and_table.py`

**Role:**
- Write MySQL connection credentials (host, user, password, port) in `db.yaml`
- In `db_connection.py`, load credentials from `db.yaml` using `PyYAML`, connect to MySQL using `mysql-connector-python`, and display a confirmation message once connection is established
- In `create_database_and_table.py`, create the `users_db` database if it does not already exist, then create the **users** table with the following fields:
  - `id`: Primary Key, Auto-Incremented
  - `username`: Unique, Required
  - `email`: Unique, Required
  - `password`
  - `city`
  - `company`
  - `job_title`
- Covers spec Q1 and Q2

### Persona 2: CRUD Developer
**Responsible files:** `create_user.py`, `read_users.py`, `update_user.py`, `delete_user.py`

**Role:**
- `create_user.py`: Accept input for username, email, password, city, company, and job title. Validate inputs, securely hash the password, and insert the new user record into the database
- `read_users.py`: Query the **users** table and display the results in a clear and formatted manner on the command line
- `update_user.py`: Allow the user to specify which field (email or password) to update. Validate and perform the update, then confirm the change
- `delete_user.py`: Accept the username as input, delete the corresponding record from the **users** table, and handle cases where the specified user does not exist
- Covers spec Q3, Q4, Q5, and Q6

### Persona 3: Data Engineer
**Responsible files:** `populate_users.py`

**Role:**
- Use the `Faker` package to generate and insert 1,000 synthetic users into the database
- Covers spec Q7

### Persona 4: UI/UX Developer
**Responsible files:** `cli_menu.py`

**Role:**
- Develop a command-line menu using the `rich` library (e.g., `rich.panel`) for enhanced UI
- Implement a menu that offers the following options:
  - Create a new user
  - Read/display one user
  - Read/display all users
  - Update an existing user
  - Delete a user
  - Exit the application
- Ensure the interface handles user inputs gracefully and routes them to the correct operations
- Covers spec Q8

### Persona 5: Integration Lead
**Responsible files:** `main.py`

**Role:**
- Integrate all previously implemented functionalities into a single executable script
- Use `main.py` as the entry point to coordinate interactions between the modules
- Ensure smooth integration and proper error handling across the application
- Covers spec Q9

## Execution Order

```
Phase 1: Persona 1 (DB Architect)     → db.yaml → db_connection.py → create_database_and_table.py
Phase 2: Persona 2 (CRUD Developer)   → create_user.py → read_users.py → update_user.py → delete_user.py
Phase 3: Persona 3 (Data Engineer)    → populate_users.py
Phase 4: Persona 4 (UI/UX Developer)  → cli_menu.py
Phase 5: Persona 5 (Integration Lead) → main.py
```

## Common Guidelines

- All code must include thorough comments to explain logic and key sections (spec: Additional Guidelines - Documentation)
- All project content (code, comments, variable names) must be written in English
- Every implementation decision must strictly follow the spec document (`docs/spec.md`)
