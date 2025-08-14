import unittest
import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from scripts.ai_utilities import preprocess_data, evaluate_model

class TestAIUtilities(unittest.TestCase):
    
    def test_preprocess_data_valid(self):
        """Test preprocess_data with valid input."""
        result = preprocess_data("  SAMPLE DATA  ")
        self.assertEqual(result, "sample data")
    
    def test_preprocess_data_invalid_type(self):
        """Test preprocess_data with invalid input type."""
        with self.assertRaises(ValueError):
            preprocess_data(123)
    
    def test_evaluate_model_perfect_accuracy(self):
        """Test evaluate_model with perfect predictions."""
        predictions = [1, 2, 3, 4]
        actuals = [1, 2, 3, 4]
        accuracy = evaluate_model(predictions, actuals)
        self.assertEqual(accuracy, 1.0)
    
    def test_evaluate_model_zero_accuracy(self):
        """Test evaluate_model with completely wrong predictions."""
        predictions = [1, 2, 3, 4]
        actuals = [5, 6, 7, 8]
        accuracy = evaluate_model(predictions, actuals)
        self.assertEqual(accuracy, 0.0)
    
    def test_evaluate_model_partial_accuracy(self):
        """Test evaluate_model with partial accuracy."""
        predictions = [1, 2, 9, 4]
        actuals = [1, 2, 3, 4]
        accuracy = evaluate_model(predictions, actuals)
        self.assertEqual(accuracy, 0.75)
    
    def test_evaluate_model_invalid_types(self):
        """Test evaluate_model with invalid input types."""
        with self.assertRaises(ValueError):
            evaluate_model("not_a_list", [1, 2, 3])
    
    def test_evaluate_model_different_lengths(self):
        """Test evaluate_model with different length lists."""
        with self.assertRaises(ValueError):
            evaluate_model([1, 2], [1, 2, 3])
    
    def test_evaluate_model_empty_lists(self):
        """Test evaluate_model with empty lists."""
        with self.assertRaises(ValueError):
            evaluate_model([], [])

if __name__ == "__main__":
    unittest.main()