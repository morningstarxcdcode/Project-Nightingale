import unittest
import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.main import main
from scripts.ai_model import simple_ai_model

class TestAI(unittest.TestCase):
    
    def test_main_function(self):
        """Test the main function returns expected result."""
        result = main()
        self.assertIn("Welcome to Project Nightingale!", result)
        self.assertIn("Processed data:", result)

    def test_simple_ai_model(self):
        """Test the simple AI model function."""
        input_data = "Test input"
        result = simple_ai_model(input_data)
        self.assertEqual(result, "Processed data: Test input")
    
    def test_simple_ai_model_validation(self):
        """Test AI model input validation."""
        with self.assertRaises(ValueError):
            simple_ai_model(123)  # Should raise error for non-string input

if __name__ == "__main__":
    unittest.main()
