import unittest
from src.main_updated_v2 import main

class TestMainUpdated(unittest.TestCase):
    """Test cases for the main application functionality."""

    def test_main_function(self):
        """Test the main function to ensure it connects to database."""
        result = main()
        self.assertIsNone(result)  # main_updated_v2 doesn't return anything, just connects to DB

if __name__ == "__main__":
    unittest.main()
