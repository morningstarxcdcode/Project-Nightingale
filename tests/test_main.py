import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main_function(self):
        self.assertEqual(main(), "Welcome to Project Nightingale!")  # Check the return value

if __name__ == "__main__":
    unittest.main()
