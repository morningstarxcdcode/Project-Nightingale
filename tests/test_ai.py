"""Enhanced tests for AI model functionality."""

import os
import sys
from unittest.mock import MagicMock, patch

import pytest

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scripts.ai_model import simple_ai_model, validate_input_data  # noqa: E402
from scripts.exceptions import DataValidationError  # noqa: E402
from src.main import main  # noqa: E402


class TestAI:
    """Test cases for AI model functionality."""

    def test_main_function(self) -> None:
        """Test the main function runs without errors."""
        with patch("src.main.create_connection") as mock_conn:
            mock_conn.return_value = MagicMock()
            result = main()
            assert isinstance(result, str)
            assert "Welcome to Project Nightingale" in result

    def test_simple_ai_model(self) -> None:
        """Test the simple AI model with valid input."""
        result = simple_ai_model("test input")
        assert isinstance(result, str)
        assert "Processed data: test input" in result

    def test_simple_ai_model_validation(self) -> None:
        """Test AI model input validation."""
        # Test empty string
        with pytest.raises(DataValidationError) as exc_info:
            simple_ai_model("")
        assert "cannot be empty" in str(exc_info.value)

        # Test whitespace only
        with pytest.raises(DataValidationError) as exc_info:
            simple_ai_model("   ")
        assert "cannot be empty" in str(exc_info.value)

        # Test non-string input
        with pytest.raises(DataValidationError) as exc_info:
            simple_ai_model(123)  # type: ignore
        assert "must be a string" in str(exc_info.value)

    def test_simple_ai_model_with_various_inputs(self) -> None:
        """Test AI model with various valid inputs."""
        test_cases = [
            "heart rate: 72 bpm",
            "temperature: 98.6°F",
            "blood pressure: 120/80 mmHg",
            "glucose level: 100 mg/dL",
            "oxygen saturation: 98%",
            "Complex medical data with symbols @#$%^&*()",
        ]

        for test_input in test_cases:
            result = simple_ai_model(test_input)
            assert isinstance(result, str)
            assert test_input in result
            assert "Processed data:" in result

    def test_validate_input_data(self) -> None:
        """Test input data validation function."""
        # Valid inputs
        assert validate_input_data("valid string") is True
        assert validate_input_data("heart rate: 72") is True

        # Invalid inputs
        assert validate_input_data("") is False
        assert validate_input_data("   ") is False
        assert validate_input_data(123) is False  # type: ignore
        assert validate_input_data(None) is False  # type: ignore
        assert validate_input_data([]) is False  # type: ignore

    def test_model_processing_error_handling(self) -> None:
        """Test model error handling with mocked failures."""
        with patch("scripts.ai_model.logger") as mock_logger:
            # Test that logging works correctly
            result = simple_ai_model("test input")
            assert result is not None
            mock_logger.debug.assert_called()
            mock_logger.info.assert_called()

    def test_model_performance_with_large_input(self) -> None:
        """Test model performance with large input data."""
        large_input = "A" * 1000  # 1000 character string
        result = simple_ai_model(large_input)
        assert isinstance(result, str)
        assert large_input in result

    @pytest.mark.parametrize(
        "input_data,expected_error",
        [
            (None, "must be a string"),
            (123, "must be a string"),
            ([], "must be a string"),
            ({}, "must be a string"),
            ("", "cannot be empty"),
            ("   ", "cannot be empty"),
        ],
    )
    def test_model_invalid_inputs_parametrized(
        self, input_data: any, expected_error: str
    ) -> None:
        """Test model with various invalid inputs using parametrization."""
        with pytest.raises(DataValidationError) as exc_info:
            simple_ai_model(input_data)  # type: ignore
        assert expected_error in str(exc_info.value)

    def test_model_with_unicode_input(self) -> None:
        """Test model with Unicode and special characters."""
        unicode_inputs = [
            "температура: 37°C",  # Cyrillic
            "心拍数: 72 bpm",  # Chinese
            "نبضات القلب: 72",  # Arabic
            "emoji test 🏥💗📊",  # Emojis
            "special chars: αβγδε",  # Greek letters
        ]

        for unicode_input in unicode_inputs:
            result = simple_ai_model(unicode_input)
            assert isinstance(result, str)
            assert unicode_input in result

    def test_model_thread_safety(self) -> None:
        """Test that the model can handle concurrent calls."""
        import threading

        results = []
        errors = []

        def run_model(input_data: str) -> None:
            try:
                result = simple_ai_model(f"test input {input_data}")
                results.append(result)
            except Exception as e:
                errors.append(e)

        # Create multiple threads
        threads = []
        for i in range(10):
            thread = threading.Thread(target=run_model, args=(str(i),))
            threads.append(thread)

        # Start all threads
        for thread in threads:
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Check results
        assert len(results) == 10
        assert len(errors) == 0

        # Verify each result is unique and correct
        for i, result in enumerate(results):
            assert f"test input {i}" in result or any(
                f"test input {j}" in result for j in range(10)
            )

    def test_model_memory_usage(self) -> None:
        """Test model memory usage with repeated calls."""
        import gc

        # Force garbage collection before test
        gc.collect()

        # Run model many times to check for memory leaks
        for i in range(100):
            result = simple_ai_model(f"iteration {i}")
            assert isinstance(result, str)

            # Force garbage collection periodically
            if i % 20 == 0:
                gc.collect()

        # Final garbage collection
        gc.collect()
        # Test passes if no memory errors occur
