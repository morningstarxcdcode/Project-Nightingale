"""Custom exception classes for Project Nightingale."""

from typing import Any, Optional


class NightingaleError(Exception):
    """Base exception class for Project Nightingale."""
    
    def __init__(self, message: str, error_code: Optional[str] = None) -> None:
        super().__init__(message)
        self.message = message
        self.error_code = error_code


class DataValidationError(NightingaleError):
    """Raised when data validation fails."""
    
    def __init__(self, message: str, invalid_data: Any = None) -> None:
        super().__init__(message, "DATA_VALIDATION_ERROR")
        self.invalid_data = invalid_data


class ModelProcessingError(NightingaleError):
    """Raised when AI model processing fails."""
    
    def __init__(self, message: str, model_name: Optional[str] = None) -> None:
        super().__init__(message, "MODEL_PROCESSING_ERROR")
        self.model_name = model_name


class DatabaseConnectionError(NightingaleError):
    """Raised when database connection fails."""
    
    def __init__(self, message: str, db_path: Optional[str] = None) -> None:
        super().__init__(message, "DATABASE_CONNECTION_ERROR")
        self.db_path = db_path


class ConfigurationError(NightingaleError):
    """Raised when configuration is invalid."""
    
    def __init__(self, message: str, config_key: Optional[str] = None) -> None:
        super().__init__(message, "CONFIGURATION_ERROR")
        self.config_key = config_key