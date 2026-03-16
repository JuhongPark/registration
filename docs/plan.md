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

### Persona 6: Reviewer
**Responsible files:** All files

**Role:**
- Review code produced by other personas against the spec document (`docs/spec.md`)
- Check for: spec compliance, correct file placement, input validation, error handling, code comments, and module interface consistency
- Produce a review report listing issues found with severity (critical / minor)
- Critical issues MUST be fixed before proceeding; minor issues SHOULD be fixed

## Execution Order

### Round 1: Implementation + Execution Testing (Phases 1–20)

All review phases include **actual execution** against a live MySQL database.

```
Phase 1:  Persona 1 (DB Architect)       → Implement db.yaml, db_connection.py, create_database_and_table.py
Phase 2:  Persona 6 (Reviewer)           → Run db_connection.py and create_database_and_table.py, verify DB/table created
Phase 3:  Persona 1 (DB Architect)       → Fix issues from review (if any)
Phase 4:  Persona 6 (Reviewer)           → Re-run and verify fixes

Phase 5:  Persona 2 (CRUD Developer)     → Implement create_user.py, read_users.py, update_user.py, delete_user.py
Phase 6:  Persona 6 (Reviewer)           → Run each CRUD module against live DB, verify data changes
Phase 7:  Persona 2 (CRUD Developer)     → Fix issues from review (if any)
Phase 8:  Persona 6 (Reviewer)           → Re-run and verify fixes

Phase 9:  Persona 3 (Data Engineer)      → Implement populate_users.py
Phase 10: Persona 6 (Reviewer)           → Run populate_users.py, verify 1,000 rows inserted
Phase 11: Persona 3 (Data Engineer)      → Fix issues from review (if any)
Phase 12: Persona 6 (Reviewer)           → Re-run and verify fixes

Phase 13: Persona 4 (UI/UX Developer)    → Implement cli_menu.py
Phase 14: Persona 6 (Reviewer)           → Run cli_menu.py with piped inputs, verify all menu paths
Phase 15: Persona 4 (UI/UX Developer)    → Fix issues from review (if any)
Phase 16: Persona 6 (Reviewer)           → Re-run and verify fixes

Phase 17: Persona 5 (Integration Lead)   → Implement main.py
Phase 18: Persona 6 (Reviewer)           → Run main.py end-to-end, verify full workflow
Phase 19: All relevant personas           → Fix final review issues (if any)
Phase 20: Persona 6 (Reviewer)           → Final sign-off for Round 1
```

### Round 2: Refinement + Hardening (Phases 21–40)

Improve code quality, edge case handling, UX polish, and robustness.

```
Phase 21: Persona 1 (DB Architect)       → Improve error handling and connection robustness
Phase 22: Persona 6 (Reviewer)           → Test with bad credentials, missing db.yaml, DB already exists
Phase 23: Persona 1 (DB Architect)       → Fix issues from review (if any)
Phase 24: Persona 6 (Reviewer)           → Re-run and verify fixes

Phase 25: Persona 2 (CRUD Developer)     → Improve validation, edge cases (duplicates, empty inputs, long strings)
Phase 26: Persona 6 (Reviewer)           → Test CRUD with edge case inputs against live DB
Phase 27: Persona 2 (CRUD Developer)     → Fix issues from review (if any)
Phase 28: Persona 6 (Reviewer)           → Re-run and verify fixes

Phase 29: Persona 3 (Data Engineer)      → Improve populate performance and reliability
Phase 30: Persona 6 (Reviewer)           → Run populate on clean DB, verify count and data quality
Phase 31: Persona 3 (Data Engineer)      → Fix issues from review (if any)
Phase 32: Persona 6 (Reviewer)           → Re-run and verify fixes

Phase 33: Persona 4 (UI/UX Developer)    → Improve menu UX (rich tables for read, better prompts, input feedback)
Phase 34: Persona 6 (Reviewer)           → Run menu with all paths, verify enhanced UI output
Phase 35: Persona 4 (UI/UX Developer)    → Fix issues from review (if any)
Phase 36: Persona 6 (Reviewer)           → Re-run and verify fixes

Phase 37: Persona 5 (Integration Lead)   → Improve main.py error handling and module coordination
Phase 38: Persona 6 (Reviewer)           → Full end-to-end test: fresh DB → populate → CRUD → menu
Phase 39: All relevant personas           → Fix final issues (if any)
Phase 40: Persona 6 (Reviewer)           → Final sign-off — project complete
```

## Review Checklist (Persona 6)

Per-phase reviews check:
1. **Spec compliance** — Does the code do exactly what the spec question asks? No more, no less
2. **File placement** — Is the logic in the correct file as specified by the spec?
3. **Input validation & error handling** — Are edge cases handled gracefully?
4. **Documentation** — Are comments thorough and explain logic and key sections?
5. **Interface consistency** — Do modules expose functions that other modules can cleanly import?
6. **Execution test** — Does the code actually run and produce correct results against a live MySQL database?

Final reviews (Phase 18, 38) additionally check:
7. **End-to-end integration** — Does `main.py` correctly coordinate all modules?
8. **Dependency consistency** — Are all required packages (`mysql-connector-python`, `PyYAML`, `Faker`, `rich`) used where specified?

## Common Guidelines

- All code must include thorough comments to explain logic and key sections (spec: Additional Guidelines - Documentation)
- All project content (code, comments, variable names) must be written in English
- Every implementation decision must strictly follow the spec document (`docs/spec.md`)
- Commits should be made at natural breakpoints throughout the process, not tied to phase boundaries
- All review phases MUST include actual execution testing against a live MySQL database
