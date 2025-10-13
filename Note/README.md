# Note Web App

This is a simple web application for taking notes.

## Setup

### 1\. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 2\. Set up the Database

This application uses a PostgreSQL database.

1.  Make sure you have PostgreSQL installed and running.
2.  Create a database named `postgres`.
3.  Create a user `postgres` with a password.

### 3\. Configure Environment Variables

Create a file named `.env` in the `Note` directory and add the following line, replacing `your_password` with the actual password for your `postgres` user:

```
DB_PW=your_password
```

### 4\. Create the Database Schema

Create the `notes` table in your `postgres` database by running the `schema.sql` file:

```bash
psql -U postgres -d postgres -a -f schema.sql
```

### 5\. Run the Application

Start the web application by running the `app.py` file:

```bash
python app.py
```

The application will be running at `http://localhost:8080`.