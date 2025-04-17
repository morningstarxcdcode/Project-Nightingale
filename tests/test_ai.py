import unittest
from src.main import main  # Ensure main is correctly imported
from scripts.ai_model import simple_ai_model

class TestAI(unittest.TestCase):
    
    def test_main_function(self):
        result = main()
        self.assertIn("Welcome to Project Nightingale!", result)

    def test_simple_ai_model(self):
        input_data = "Test input"
        result = simple_ai_model(input_data)
        self.assertEqual(result, "Processed data: Test input")
from scripts.ai_model import simple_ai_model

class TestAI(unittest.TestCase):
    
    def test_main_function(self):
        result = main()
        self.assertIn("Welcome to Project Nightingale!", result)

    def test_simple_ai_model(self):
        input_data = "Test input"
        result = simple_ai_model(input_data)
        self.assertEqual(result, "Processed data: Test input")

if __name__ == "__main__":
    unittest.main()
