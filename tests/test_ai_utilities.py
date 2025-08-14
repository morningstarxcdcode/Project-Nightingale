"""Enhanced tests for AI utilities functionality."""

import os
import sys
from unittest.mock import patch

import pytest

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scripts.ai_utilities import (
    calculate_metrics,
    evaluate_model,
    preprocess_data,
    validate_data_types,
)
from scripts.exceptions import DataValidationError, ModelProcessingError


class TestAIUtilities:
    """Test cases for AI utilities functionality."""

    def test_preprocess_data_valid(self) -> None:
        """Test preprocess_data with valid input."""
        result = preprocess_data("  SAMPLE DATA  ")
        assert result == "sample data"

    def test_preprocess_data_invalid_type(self) -> None:
        """Test preprocess_data with invalid input type."""
        with pytest.raises(DataValidationError) as exc_info:
            preprocess_data(123)  # type: ignore
        assert "must be a string" in str(exc_info.value)

    def test_preprocess_data_edge_cases(self) -> None:
        """Test preprocess_data with edge cases."""
        # Empty string
        assert preprocess_data("") == ""

        # Only whitespace
        assert preprocess_data("   ") == ""

        # Mixed case with special characters
        assert preprocess_data("  Hello WORLD! 123  ") == "hello world! 123"

        # Unicode characters
        assert preprocess_data("  HÉLLO WÖRLD  ") == "héllo wörld"

    def test_evaluate_model_perfect_accuracy(self) -> None:
        """Test evaluate_model with perfect predictions."""
        predictions = [1, 2, 3, 4]
        actuals = [1, 2, 3, 4]
        accuracy = evaluate_model(predictions, actuals)
        assert accuracy == 1.0

    def test_evaluate_model_zero_accuracy(self) -> None:
        """Test evaluate_model with completely wrong predictions."""
        predictions = [1, 2, 3, 4]
        actuals = [5, 6, 7, 8]
        accuracy = evaluate_model(predictions, actuals)
        assert accuracy == 0.0

    def test_evaluate_model_partial_accuracy(self) -> None:
        """Test evaluate_model with partial accuracy."""
        predictions = [1, 2, 9, 4]
        actuals = [1, 2, 3, 4]
        accuracy = evaluate_model(predictions, actuals)
        assert accuracy == 0.75

    def test_evaluate_model_invalid_types(self) -> None:
        """Test evaluate_model with invalid input types."""
        with pytest.raises(DataValidationError) as exc_info:
            evaluate_model("not_a_list", [1, 2, 3])  # type: ignore
        assert "must be lists" in str(exc_info.value)

    def test_evaluate_model_different_lengths(self) -> None:
        """Test evaluate_model with different length lists."""
        with pytest.raises(DataValidationError) as exc_info:
            evaluate_model([1, 2], [1, 2, 3])
        assert "same length" in str(exc_info.value)

    def test_evaluate_model_empty_lists(self) -> None:
        """Test evaluate_model with empty lists."""
        with pytest.raises(DataValidationError) as exc_info:
            evaluate_model([], [])
        assert "empty lists" in str(exc_info.value)

    def test_calculate_metrics_basic(self) -> None:
        """Test calculate_metrics with basic numeric data."""
        predictions = [1.0, 2.0, 3.0, 4.0]
        actuals = [1.1, 2.1, 2.9, 3.8]

        metrics = calculate_metrics(predictions, actuals)

        assert "accuracy" in metrics
        assert "mae" in metrics
        assert "mse" in metrics
        assert "rmse" in metrics
        assert "sample_count" in metrics

        assert metrics["sample_count"] == 4
        assert 0 <= metrics["accuracy"] <= 1
        assert metrics["mae"] >= 0
        assert metrics["mse"] >= 0
        assert metrics["rmse"] >= 0

    def test_calculate_metrics_perfect_predictions(self) -> None:
        """Test calculate_metrics with perfect predictions."""
        predictions = [1, 2, 3, 4]
        actuals = [1, 2, 3, 4]

        metrics = calculate_metrics(predictions, actuals)

        assert metrics["accuracy"] == 1.0
        assert metrics["mae"] == 0.0
        assert metrics["mse"] == 0.0
        assert metrics["rmse"] == 0.0

    def test_validate_data_types(self) -> None:
        """Test validate_data_types function."""
        # Valid types
        assert validate_data_types("string", (str,)) is True
        assert validate_data_types(123, (int, float)) is True
        assert validate_data_types(12.5, (int, float)) is True
        assert validate_data_types([1, 2, 3], (list, tuple)) is True

        # Invalid types
        assert validate_data_types("string", (int,)) is False
        assert validate_data_types(123, (str,)) is False
        assert validate_data_types([], (dict,)) is False

    @pytest.mark.parametrize(
        "predictions,actuals,expected_accuracy",
        [
            ([1, 1, 1, 1], [1, 1, 1, 1], 1.0),
            ([1, 0, 1, 0], [0, 0, 0, 0], 0.5),
            ([True, False, True], [True, False, True], 1.0),
            (["a", "b", "c"], ["a", "x", "c"], 2 / 3),
        ],
    )
    def test_evaluate_model_parametrized(
        self, predictions: list, actuals: list, expected_accuracy: float
    ) -> None:
        """Test evaluate_model with various input combinations."""
        accuracy = evaluate_model(predictions, actuals)
        assert (
            abs(accuracy - expected_accuracy) < 0.001
        )  # Allow for floating point precision

    def test_preprocess_data_with_logging(self) -> None:
        """Test preprocess_data logging functionality."""
        with patch("scripts.ai_utilities.logger") as mock_logger:
            result = preprocess_data("TEST DATA")
            assert result == "test data"
            mock_logger.debug.assert_called()

    def test_evaluate_model_with_logging(self) -> None:
        """Test evaluate_model logging functionality."""
        with patch("scripts.ai_utilities.logger") as mock_logger:
            accuracy = evaluate_model([1, 2, 3], [1, 2, 3])
            assert accuracy == 1.0
            mock_logger.debug.assert_called()
            mock_logger.info.assert_called()

    def test_large_dataset_performance(self) -> None:
        """Test utilities performance with large datasets."""
        import time

        # Create large datasets
        size = 10000
        predictions = list(range(size))
        actuals = list(range(size))

        # Measure evaluation time
        start_time = time.time()
        accuracy = evaluate_model(predictions, actuals)
        end_time = time.time()

        assert accuracy == 1.0
        assert (end_time - start_time) < 1.0  # Should complete within 1 second

    def test_mixed_data_types_in_evaluation(self) -> None:
        """Test evaluate_model with mixed data types."""
        # String comparisons
        predictions = ["apple", "banana", "cherry"]
        actuals = ["apple", "orange", "cherry"]
        accuracy = evaluate_model(predictions, actuals)
        assert accuracy == 2 / 3

        # Boolean comparisons
        predictions = [True, False, True, False]
        actuals = [True, True, False, False]
        accuracy = evaluate_model(predictions, actuals)
        assert accuracy == 0.5

        # Mixed comparisons (not recommended but should work)
        predictions = [1, "test", True]
        actuals = [1, "test", False]
        accuracy = evaluate_model(predictions, actuals)
        assert accuracy == 2 / 3

    def test_error_propagation_in_calculate_metrics(self) -> None:
        """Test error propagation in calculate_metrics."""
        # Test with invalid data that should raise DataValidationError
        with pytest.raises(DataValidationError):
            calculate_metrics([], [])  # Empty lists

        with pytest.raises(DataValidationError):
            calculate_metrics([1, 2], [1])  # Different lengths

    def test_unicode_preprocessing(self) -> None:
        """Test preprocessing with various Unicode characters."""
        test_cases = [
            ("  HÉLLO WÖRLD  ", "héllo wörld"),
            ("  МОСКВА  ", "москва"),
            ("  北京  ", "北京"),
            ("  🏥 HOSPITAL 🏥  ", "🏥 hospital 🏥"),
            ("  MiXeD CaSe WiTh ÑÚMBÉRS 123  ", "mixed case with ñúmbérs 123"),
        ]

        for input_text, expected in test_cases:
            result = preprocess_data(input_text)
            assert result == expected

    def test_memory_efficiency(self) -> None:
        """Test memory efficiency with repeated operations."""
        import gc

        # Force garbage collection
        gc.collect()

        # Perform many preprocessing operations
        for i in range(1000):
            result = preprocess_data(f"  TEST DATA {i}  ")
            assert result == f"test data {i}"

            # Periodic cleanup
            if i % 100 == 0:
                gc.collect()

        # Final cleanup
        gc.collect()
        # Test passes if no memory issues occur
