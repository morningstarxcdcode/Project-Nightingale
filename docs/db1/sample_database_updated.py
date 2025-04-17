import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create a table in the database."""
    try:
        sql_create_table = """CREATE TABLE IF NOT EXISTS users (
                                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                                  name TEXT NOT NULL,
                                  email TEXT NOT NULL UNIQUE
                              );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(e)

def insert_user(conn, name, email):
    """Insert a new user into the users table."""
    try:
        sql_insert_user = """INSERT INTO users (name, email) VALUES (?, ?);"""
        cursor = conn.cursor()
        cursor.execute(sql_insert_user, (name, email))
        conn.commit()
        print("User inserted successfully.")
    except sqlite3.Error as e:
        print(e)

def main():
    database = "project_nightingale.db"
    conn = create_connection(database)
    create_table(conn)

if __name__ == '__main__':
    main()
