import unittest
from src.main import main

class TestMainUpdated(unittest.TestCase):
    def test_main_function(self):
        result = main()
        self.assertIn("AI Result:", result)  # Check if the result contains the AI output

if __name__ == "__main__":
    unittest.main()
