# Main application file for Project Nightingale

import os
import sys
import sqlite3

# Add the scripts directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from ai_model import simple_ai_model
from ai_utilities import preprocess_data, evaluate_model

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def main(database="project_nightingale.db"):
    conn = create_connection(database)


if __name__ == '__main__':
    result = main()
    print(result)
