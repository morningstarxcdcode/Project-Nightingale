"""Main application file for Project Nightingale."""

import logging
import os
import sqlite3
import sys
from pathlib import Path
from typing import Optional

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(project_root, ".."))

from scripts.ai_model import simple_ai_model  # noqa: E402
from scripts.ai_utilities import preprocess_data  # noqa: E402
from scripts.config import get_config  # noqa: E402
from scripts.exceptions import (  # noqa: E402
    DatabaseConnectionError,
    DataValidationError,
    NightingaleError,
)

logger = logging.getLogger(__name__)


def setup_logging() -> None:
    """Setup logging configuration."""
    try:
        config = get_config()
        log_level = getattr(logging, config.get("logging.level", "INFO").upper())
        log_format = config.get("logging.format")
        log_file = config.get("logging.file")

        # Configure logging
        logging.basicConfig(
            level=log_level,
            format=log_format,
            filename=log_file,
            filemode="a" if log_file else None,
        )

        # Also log to console if file logging is enabled
        if log_file:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)
            console_handler.setFormatter(logging.Formatter(log_format))
            logging.getLogger().addHandler(console_handler)

    except Exception as e:
        # Fallback to basic logging if config fails
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logger.warning(f"Failed to setup logging from config: {e}")


def create_connection(db_file: str) -> Optional[sqlite3.Connection]:
    """
    Create a database connection to the SQLite database specified by db_file.

    Args:
        db_file (str): Path to the database file.

    Returns:
        Optional[sqlite3.Connection]: Database connection or None if failed.

    Raises:
        DatabaseConnectionError: If connection fails.
    """
    if not db_file:
        raise DatabaseConnectionError("Database file path cannot be empty")

    try:
        # Ensure directory exists
        db_path = Path(db_file)
        db_path.parent.mkdir(parents=True, exist_ok=True)

        # Get timeout from config
        config = get_config()
        timeout = config.get("database.timeout", 30)

        conn = sqlite3.connect(db_file, timeout=timeout)
        conn.row_factory = sqlite3.Row  # Enable column access by name

        logger.info(f"Connected to database: {db_file}")
        return conn

    except sqlite3.Error as e:
        logger.error(f"Database connection error: {e}")
        raise DatabaseConnectionError(
            f"Failed to connect to database {db_file}: {str(e)}", db_path=db_file
        ) from e


def initialize_database(conn: sqlite3.Connection) -> None:
    """
    Initialize the database with required tables.

    Args:
        conn (sqlite3.Connection): Database connection.
    """
    try:
        cursor = conn.cursor()

        # Create a simple table for storing analysis results
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS analysis_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                input_data TEXT NOT NULL,
                processed_data TEXT NOT NULL,
                success BOOLEAN DEFAULT TRUE
            )
        """
        )

        conn.commit()
        logger.debug("Database initialized successfully")

    except sqlite3.Error as e:
        logger.error(f"Database initialization failed: {e}")
        raise DatabaseConnectionError(f"Failed to initialize database: {str(e)}") from e


def save_analysis_result(
    conn: sqlite3.Connection, input_data: str, processed_data: str, success: bool = True
) -> None:
    """
    Save analysis result to database.

    Args:
        conn (sqlite3.Connection): Database connection.
        input_data (str): Original input data.
        processed_data (str): Processed result data.
        success (bool): Whether processing was successful.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO analysis_results (input_data, processed_data, success)
            VALUES (?, ?, ?)
        """,
            (input_data, processed_data, success),
        )

        conn.commit()
        logger.debug("Analysis result saved to database")

    except sqlite3.Error as e:
        logger.warning(f"Failed to save analysis result: {e}")
        # Don't raise exception as this is not critical


def validate_input(input_data: str) -> None:
    """
    Validate input data according to configuration constraints.

    Args:
        input_data (str): Input data to validate.

    Raises:
        DataValidationError: If input is invalid.
    """
    config = get_config()
    max_length = config.get("ai.max_input_length", 10000)

    if not isinstance(input_data, str):
        raise DataValidationError(
            f"Input data must be a string, got {type(input_data).__name__}",
            invalid_data=input_data,
        )

    if len(input_data) > max_length:
        raise DataValidationError(
            f"Input data too long: {len(input_data)} characters (max: {max_length})",
            invalid_data=input_data,
        )


def main(database: Optional[str] = None, input_data: Optional[str] = None) -> str:
    """
    Main function that runs the Project Nightingale application.

    Args:
        database (Optional[str]): Database file path. If None, uses config default.
        input_data (Optional[str]): Input data to process. If None, uses default.

    Returns:
        str: Result message from the AI processing.

    Raises:
        NightingaleError: If processing fails.
    """
    try:
        # Setup logging
        setup_logging()
        logger.info("Starting Project Nightingale...")

        # Load configuration
        config = get_config()
        config.validate()

        # Determine database path
        if database is None:
            database = config.get("database.file", "project_nightingale.db")

        # Create database connection
        db_path = os.path.join(os.path.dirname(__file__), "..", database)
        conn = create_connection(db_path)

        if conn is None:
            raise DatabaseConnectionError("Failed to establish database connection")

        # Initialize database
        initialize_database(conn)

        # Use provided input or default
        if input_data is None:
            input_data = "Sample health data input"

        # Validate input
        validate_input(input_data)

        # Preprocess the input data
        logger.debug("Preprocessing input data...")
        preprocessed_data = preprocess_data(input_data)

        # Process with AI model
        logger.debug("Processing with AI model...")
        result = simple_ai_model(preprocessed_data)

        if result is None:
            raise ValueError("AI model returned None result")

        logger.info("AI processing completed successfully")

        # Save result to database
        save_analysis_result(conn, input_data, result, success=True)

        # Close database connection
        conn.close()
        logger.info("Database connection closed")

        return f"Welcome to Project Nightingale! AI Result: {result}"

    except NightingaleError:
        # Re-raise our custom exceptions
        raise
    except Exception as e:
        logger.error(f"Unexpected error in main: {e}")
        raise NightingaleError(
            f"Application failed with unexpected error: {str(e)}"
        ) from e
    finally:
        # Ensure database connection is closed
        if "conn" in locals() and conn:
            try:
                conn.close()
            except sqlite3.Error:
                pass


if __name__ == "__main__":
    try:
        result = main()
        print(result)
        sys.exit(0)
    except NightingaleError as e:
        logger.error(f"Application error: {e.message}")
        print(f"Error: {e.message}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
        sys.exit(1)
