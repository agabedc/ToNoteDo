# Database Setup
Each teammate creates their own local database.

## Install PostgreSQL & pgAdmin

```bash
brew install postgresql@16
brew services start postgresql@16
```

## Create Database and App User (using pgAdmin)
1. Open pgAdmin → Servers → connect to PostgreSQL 
2. Right-click Login/Group Roles → Create → Login/Group Role…
- General → Name: team_app
- Definition → Password: set a password (e.g., slowapi)
- Privileges: Leave defaults (no superuser).
- Save.
3. Right-click Databases → Create → Database…
- Database: todo
- Owner: team_app (or set owner to postgres and grant later)
- Save.
4. Grant privileges (if owner is not team_app):
In pgAdmin, open Tools → Query Tool connected to todo and run:
```bash
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE public.tasks TO team_app;

GRANT USAGE, SELECT ON SEQUENCE public.tasks_id_seq TO team_app;

ALTER TABLE public.tasks OWNER TO team_app;
ALTER SEQUENCE public.tasks_id_seq OWNER TO team_app;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO team_app;

ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT USAGE, SELECT ON SEQUENCES TO team_app;
```

## Create Tables (schema)
Copy the schema.sql (already in ToDo/backend) and run it by choosing Tools → Query Tool → open schema.sql → ▶ Execute.

## App Configuration (.env)
Create a .env file in backend/ (same folder as app.py and db.py):
```bash
DB_NAME=todo
DB_USER=team_app
DB_PASSWORD=slowapi
DB_HOST=127.0.0.1
DB_PORT=5432
```
## Run the App
From the project’s backend/:
```bash
python3 -m venv venv
source venv/bin/activate     
pip install -r requirements.txt
python app.py
```