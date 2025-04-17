import unittest
from src.main_updated_v51 import main  # Ensure the correct import

class TestAI(unittest.TestCase):
    
    def test_main_function(self):
        # Test the main function
        result = main()
        self.assertIn("Processed data:", result)  # Check if the result contains the AI output

if __name__ == "__main__":
    unittest.main()
