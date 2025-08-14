import unittest
from src.main_updated_v2 import main  # Ensure the correct import

class TestAI(unittest.TestCase):
    
    def test_main_function(self):
        # Test the main function - it connects to database but doesn't return anything
        result = main()
        self.assertIsNone(result)  # main_updated_v2 doesn't return anything

if __name__ == '__main__':
    unittest.main()
