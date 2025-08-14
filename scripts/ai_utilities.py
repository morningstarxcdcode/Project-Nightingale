"""Utility functions for AI in Project Nightingale."""

from typing import List, Union, Any, Tuple, Optional, Dict
import logging
from .exceptions import DataValidationError, ModelProcessingError

logger = logging.getLogger(__name__)


def preprocess_data(data: str) -> str:
    """
    Preprocess the input data for the AI model.
    
    This function normalizes and cleans input data to ensure consistent
    processing by downstream AI models.
    
    Args:
        data (str): The input data to preprocess.
    
    Returns:
        str: The preprocessed data (trimmed and lowercased).
    
    Raises:
        DataValidationError: If data is not a string.
    
    Example:
        >>> result = preprocess_data("  HEART RATE: 72 BPM  ")
        >>> print(result)
        heart rate: 72 bpm
    """
    logger.debug(f"Preprocessing data: {str(data)[:50]}...")
    
    if not isinstance(data, str):
        raise DataValidationError(
            f"Data must be a string, got {type(data).__name__}",
            invalid_data=data
        )
    
    # Preprocessing pipeline:
    # 1. Strip whitespace
    # 2. Convert to lowercase
    # 3. Future: Could add more sophisticated preprocessing like:
    #    - Text normalization
    #    - Feature extraction
    #    - Data validation
    preprocessed = data.strip().lower()
    
    logger.debug(f"Data preprocessed successfully: {len(preprocessed)} characters")
    return preprocessed


def evaluate_model(predictions: List[Any], actuals: List[Any]) -> float:
    """
    Evaluate the AI model's predictions against actual values.
    
    Calculates accuracy as the proportion of correct predictions.
    
    Args:
        predictions (List[Any]): List of predicted values.
        actuals (List[Any]): List of actual values.
    
    Returns:
        float: Accuracy score between 0.0 and 1.0.
    
    Raises:
        DataValidationError: If inputs are invalid or mismatched.
    
    Example:
        >>> predictions = [1, 0, 1, 1]
        >>> actuals = [1, 0, 0, 1]
        >>> accuracy = evaluate_model(predictions, actuals)
        >>> print(f"Accuracy: {accuracy:.2f}")
        Accuracy: 0.75
    """
    logger.debug(f"Evaluating model with {len(predictions)} predictions")
    
    # Input validation
    if not isinstance(predictions, list) or not isinstance(actuals, list):
        raise DataValidationError(
            "Predictions and actuals must be lists",
            invalid_data={"predictions_type": type(predictions).__name__, 
                         "actuals_type": type(actuals).__name__}
        )
    
    if len(predictions) != len(actuals):
        raise DataValidationError(
            f"Predictions and actuals must have the same length. "
            f"Got {len(predictions)} predictions and {len(actuals)} actuals",
            invalid_data={"predictions_len": len(predictions), 
                         "actuals_len": len(actuals)}
        )
    
    if len(predictions) == 0:
        raise DataValidationError(
            "Cannot evaluate with empty lists",
            invalid_data={"length": 0}
        )
    
    # Calculate accuracy
    try:
        correct_predictions = sum(p == a for p, a in zip(predictions, actuals))
        accuracy = correct_predictions / len(actuals)
        
        logger.info(f"Model evaluation complete: {correct_predictions}/{len(actuals)} "
                   f"correct (accuracy: {accuracy:.3f})")
        
        return accuracy
        
    except Exception as e:
        logger.error(f"Model evaluation failed: {e}")
        raise ModelProcessingError(
            f"Failed to evaluate model predictions: {str(e)}"
        ) from e


def calculate_metrics(predictions: List[Union[int, float]], 
                     actuals: List[Union[int, float]]) -> Dict[str, float]:
    """
    Calculate comprehensive evaluation metrics for model performance.
    
    Args:
        predictions (List[Union[int, float]]): List of predicted values.
        actuals (List[Union[int, float]]): List of actual values.
    
    Returns:
        Dict[str, float]: Dictionary containing various metrics.
    
    Raises:
        DataValidationError: If inputs are invalid.
    """
    accuracy = evaluate_model(predictions, actuals)
    
    # Calculate additional metrics
    try:
        # Mean Absolute Error
        mae = sum(abs(p - a) for p, a in zip(predictions, actuals)) / len(actuals)
        
        # Mean Squared Error
        mse = sum((p - a) ** 2 for p, a in zip(predictions, actuals)) / len(actuals)
        
        # Root Mean Squared Error
        rmse = mse ** 0.5
        
        metrics = {
            "accuracy": accuracy,
            "mae": mae,
            "mse": mse,
            "rmse": rmse,
            "sample_count": len(actuals)
        }
        
        logger.info(f"Calculated metrics: {metrics}")
        return metrics
        
    except Exception as e:
        logger.error(f"Metrics calculation failed: {e}")
        raise ModelProcessingError(
            f"Failed to calculate metrics: {str(e)}"
        ) from e


def validate_data_types(data: Any, expected_types: Tuple[type, ...]) -> bool:
    """
    Validate that data matches expected types.
    
    Args:
        data: The data to validate.
        expected_types: Tuple of expected types.
    
    Returns:
        bool: True if data type is valid, False otherwise.
    """
    return isinstance(data, expected_types)
