"""Tests for custom exception classes."""

import os
import sys

import pytest

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scripts.exceptions import (  # noqa: E402
    ConfigurationError,
    DatabaseConnectionError,
    DataValidationError,
    ModelProcessingError,
    NightingaleError,
)


class TestCustomExceptions:
    """Test cases for custom exception classes."""

    def test_nightingale_error_base(self) -> None:
        """Test base NightingaleError class."""
        error = NightingaleError("Test error message")

        assert str(error) == "Test error message"
        assert error.message == "Test error message"
        assert error.error_code is None

        # Test with error code
        error_with_code = NightingaleError("Test error", "TEST_CODE")
        assert error_with_code.message == "Test error"
        assert error_with_code.error_code == "TEST_CODE"

    def test_data_validation_error(self) -> None:
        """Test DataValidationError class."""
        invalid_data = {"key": "value"}
        error = DataValidationError("Invalid data format", invalid_data)

        assert str(error) == "Invalid data format"
        assert error.message == "Invalid data format"
        assert error.error_code == "DATA_VALIDATION_ERROR"
        assert error.invalid_data == invalid_data

        # Test without invalid_data
        error_no_data = DataValidationError("Invalid format")
        assert error_no_data.invalid_data is None

    def test_model_processing_error(self) -> None:
        """Test ModelProcessingError class."""
        error = ModelProcessingError("Model failed", "simple_ai_model")

        assert str(error) == "Model failed"
        assert error.message == "Model failed"
        assert error.error_code == "MODEL_PROCESSING_ERROR"
        assert error.model_name == "simple_ai_model"

        # Test without model_name
        error_no_name = ModelProcessingError("Processing failed")
        assert error_no_name.model_name is None

    def test_database_connection_error(self) -> None:
        """Test DatabaseConnectionError class."""
        db_path = "/path/to/database.db"
        error = DatabaseConnectionError("Connection failed", db_path)

        assert str(error) == "Connection failed"
        assert error.message == "Connection failed"
        assert error.error_code == "DATABASE_CONNECTION_ERROR"
        assert error.db_path == db_path

        # Test without db_path
        error_no_path = DatabaseConnectionError("Database error")
        assert error_no_path.db_path is None

    def test_configuration_error(self) -> None:
        """Test ConfigurationError class."""
        config_key = "app.database.host"
        error = ConfigurationError("Invalid configuration", config_key)

        assert str(error) == "Invalid configuration"
        assert error.message == "Invalid configuration"
        assert error.error_code == "CONFIGURATION_ERROR"
        assert error.config_key == config_key

        # Test without config_key
        error_no_key = ConfigurationError("Config error")
        assert error_no_key.config_key is None

    def test_exception_inheritance(self) -> None:
        """Test that all custom exceptions inherit from NightingaleError."""
        assert issubclass(DataValidationError, NightingaleError)
        assert issubclass(ModelProcessingError, NightingaleError)
        assert issubclass(DatabaseConnectionError, NightingaleError)
        assert issubclass(ConfigurationError, NightingaleError)

        # Test that they're also Exception subclasses
        assert issubclass(NightingaleError, Exception)
        assert issubclass(DataValidationError, Exception)

    def test_exception_chaining(self) -> None:
        """Test exception chaining with custom exceptions."""
        original_error = ValueError("Original error")

        try:
            raise original_error
        except ValueError as e:
            chained_error = ModelProcessingError("Model failed due to input error")
            chained_error.__cause__ = e

            assert chained_error.__cause__ is original_error
            assert str(chained_error) == "Model failed due to input error"

    def test_exception_catching(self) -> None:
        """Test catching custom exceptions."""
        # Test catching specific exception
        with pytest.raises(DataValidationError) as exc_info:
            raise DataValidationError("Test error", {"data": "invalid"})

        caught_error = exc_info.value
        assert caught_error.message == "Test error"
        assert caught_error.invalid_data == {"data": "invalid"}

        # Test catching base exception
        with pytest.raises(NightingaleError):
            raise ModelProcessingError("Model error")

        # Test catching as general Exception
        with pytest.raises(Exception):
            raise ConfigurationError("Config error")

    def test_exception_attributes_immutable(self) -> None:
        """Test that exception attributes are set correctly."""
        error = DataValidationError("Test message", {"key": "value"})

        # Attributes should be accessible
        assert hasattr(error, "message")
        assert hasattr(error, "error_code")
        assert hasattr(error, "invalid_data")

        # Test that we can access all attributes
        assert error.message == "Test message"
        assert error.error_code == "DATA_VALIDATION_ERROR"
        assert error.invalid_data == {"key": "value"}

    def test_exception_with_complex_data(self) -> None:
        """Test exceptions with complex data structures."""
        complex_data = {
            "input_data": "user input",
            "processed_data": ["item1", "item2"],
            "metadata": {
                "timestamp": "2024-01-01T00:00:00Z",
                "user_id": 12345,
                "nested": {"level": 3, "values": [1, 2, 3]},
            },
        }

        error = DataValidationError("Complex validation error", complex_data)

        assert error.invalid_data == complex_data
        assert error.invalid_data["metadata"]["user_id"] == 12345
        assert error.invalid_data["metadata"]["nested"]["values"] == [1, 2, 3]

    def test_exception_error_codes(self) -> None:
        """Test that error codes are set correctly for each exception type."""
        exceptions_and_codes = [
            (DataValidationError("msg"), "DATA_VALIDATION_ERROR"),
            (ModelProcessingError("msg"), "MODEL_PROCESSING_ERROR"),
            (DatabaseConnectionError("msg"), "DATABASE_CONNECTION_ERROR"),
            (ConfigurationError("msg"), "CONFIGURATION_ERROR"),
        ]

        for exception, expected_code in exceptions_and_codes:
            assert exception.error_code == expected_code

    def test_exception_string_representation(self) -> None:
        """Test string representation of exceptions."""
        error = DataValidationError("Validation failed")

        # __str__ should return the message
        assert str(error) == "Validation failed"

        # Test with different messages
        errors = [
            NightingaleError("Base error"),
            DataValidationError("Data error"),
            ModelProcessingError("Model error"),
            DatabaseConnectionError("DB error"),
            ConfigurationError("Config error"),
        ]

        for error in errors:
            assert str(error) == error.message

    def test_multiple_exception_scenarios(self) -> None:
        """Test multiple related exception scenarios."""
        # Scenario 1: Data validation leads to model processing error
        try:
            raise DataValidationError("Invalid input format")
        except DataValidationError as data_error:
            try:
                model_error = ModelProcessingError(
                    "Cannot process due to validation error"
                )
                model_error.__cause__ = data_error
                raise model_error
            except ModelProcessingError as model_error:
                assert model_error.__cause__ is data_error
                assert isinstance(model_error.__cause__, DataValidationError)

        # Scenario 2: Configuration error leads to database error
        try:
            raise ConfigurationError("Missing database configuration")
        except ConfigurationError as config_error:
            try:
                db_error = DatabaseConnectionError("Cannot connect due to config")
                db_error.__cause__ = config_error
                raise db_error
            except DatabaseConnectionError as db_error:
                assert db_error.__cause__ is config_error
                assert isinstance(db_error.__cause__, ConfigurationError)

    @pytest.mark.parametrize(
        "exception_class,message,extra_arg",
        [
            (DataValidationError, "Data error", {"invalid": "data"}),
            (ModelProcessingError, "Model error", "model_name"),
            (DatabaseConnectionError, "DB error", "/path/to/db"),
            (ConfigurationError, "Config error", "config.key"),
        ],
    )
    def test_exception_creation_parametrized(
        self, exception_class: type, message: str, extra_arg: any
    ) -> None:
        """Test exception creation with various parameters."""
        # Create exception with extra argument
        error = exception_class(message, extra_arg)

        assert error.message == message
        assert str(error) == message
        assert issubclass(type(error), NightingaleError)

        # Verify extra argument is stored correctly
        if exception_class == DataValidationError:
            assert error.invalid_data == extra_arg
        elif exception_class == ModelProcessingError:
            assert error.model_name == extra_arg
        elif exception_class == DatabaseConnectionError:
            assert error.db_path == extra_arg
        elif exception_class == ConfigurationError:
            assert error.config_key == extra_arg
