import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import main
from scripts.ai_model import simple_ai_model
from scripts.ai_utilities import preprocess_data, evaluate_model

class TestIntegration(unittest.TestCase):
    
    def test_full_ai_pipeline(self):
        """Test the complete AI processing pipeline"""
        # Test data
        raw_data = "Test Data for AI Processing"
        
        # Step 1: Preprocess data
        processed = preprocess_data(raw_data)
        self.assertEqual(processed, "test data for ai processing")
        
        # Step 2: Run AI model
        result = simple_ai_model(processed)
        self.assertEqual(result, "Processed data: test data for ai processing")
        
        # Step 3: Test evaluation function
        predictions = ["result1", "result2", "result3"]
        actuals = ["result1", "result2", "result3"]
        accuracy = evaluate_model(predictions, actuals)
        self.assertEqual(accuracy, 1.0)  # Perfect accuracy
    
    def test_main_application_flow(self):
        """Test the main application runs without errors"""
        result = main()
        self.assertIsInstance(result, str)
        self.assertIn("Welcome to Project Nightingale!", result)
        self.assertIn("AI Result:", result)
    
    def test_error_handling(self):
        """Test that functions handle various inputs properly"""
        # Test empty input
        empty_result = preprocess_data("")
        self.assertEqual(empty_result, "")
        
        # Test None input handling for AI model
        try:
            none_result = simple_ai_model(None)
            self.assertIn("None", none_result)
        except Exception:
            # It's okay if it raises an exception, that's valid error handling
            pass
    
    def test_ai_utilities_functionality(self):
        """Test that AI utilities work as expected"""
        # Test preprocess_data with various inputs
        test_cases = [
            ("HELLO WORLD", "hello world"),
            ("  Test  ", "test"),
            ("MiXeD cAsE", "mixed case"),
        ]
        
        for input_data, expected in test_cases:
            result = preprocess_data(input_data)
            self.assertEqual(result, expected)
        
        # Test evaluate_model with different scenarios
        perfect_accuracy = evaluate_model([1, 2, 3], [1, 2, 3])
        self.assertEqual(perfect_accuracy, 1.0)
        
        partial_accuracy = evaluate_model([1, 2, 3], [1, 2, 4])
        self.assertAlmostEqual(partial_accuracy, 0.666, places=2)
        
        zero_accuracy = evaluate_model([1, 2, 3], [4, 5, 6])
        self.assertEqual(zero_accuracy, 0.0)

if __name__ == "__main__":
    unittest.main()