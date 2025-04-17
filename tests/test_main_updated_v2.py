import unittest
from src.main_updated_v2 import main

class TestMainUpdated(unittest.TestCase):
    """Test cases for the main application functionality."""

    def test_main_function(self):
        """Test the main function to ensure it returns expected results."""
        result = main()
        self.assertIn("Processed data:", result)  # Check if the result contains the AI output

if __name__ == "__main__":
    unittest.main()
