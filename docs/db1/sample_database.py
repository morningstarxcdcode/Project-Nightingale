import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(e)
    return conn

def main():
    database = "project_nightingale.db"
    conn = create_connection(database)

if __name__ == '__main__':
    main()
