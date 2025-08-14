# Main application file for Project Nightingale

import sys
import os
import sqlite3
import logging

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(project_root, '..'))

from scripts.ai_model import simple_ai_model
from scripts.ai_utilities import preprocess_data, evaluate_model

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
    return conn

def main(database="project_nightingale.db"):
    """Main function that runs the Project Nightingale application."""
    logging.info("Starting Project Nightingale...")
    
    # Create database connection
    db_path = os.path.join(os.path.dirname(__file__), '..', database)
    conn = create_connection(db_path)
    
    # Example input data for the AI model
    input_data = "Sample health data input"
    
    # Preprocess the input data
    preprocessed_data = preprocess_data(input_data)
    
    # Process with AI model
    result = simple_ai_model(preprocessed_data)
    
    if result is None:
        return "No data processed."
    
    logging.info(f"AI Result: {result}")
    
    # Close database connection if it exists
    if conn:
        conn.close()
        logging.info("Database connection closed.")
    
    return f"Welcome to Project Nightingale! AI Result: {result}"

if __name__ == "__main__":
    result = main()
    print(result)
