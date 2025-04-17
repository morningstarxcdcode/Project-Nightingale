import unittest
from src.main_updated import create_connection
from scripts.ai_model import simple_ai_model

class TestAI(unittest.TestCase):
    
    def test_main_function(self):
        # Test the main function
        result = main()
        self.assertIsNone(result)  # Assuming main() does not return anything

    def test_database_connection(self):
        # Test database connection
        database = "project_nightingale.db"
        conn = create_connection(database)
        self.assertIsNotNone(conn)  # Ensure the connection is established

if __name__ == '__main__':
    unittest.main()
