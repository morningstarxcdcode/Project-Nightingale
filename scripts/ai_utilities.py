# Utility functions for AI in Project Nightingale

def preprocess_data(data):
    """
    Preprocess the input data for the AI model.
    
    Parameters:
    data (str): The input data to preprocess.
    
    Returns:
    str: The preprocessed data.
    
    Raises:
    ValueError: If data is not a string.
    """
    if not isinstance(data, str):
        raise ValueError("Data must be a string.")
    
    # Placeholder for preprocessing logic
    # In a real implementation, this might include:
    # - Text normalization
    # - Feature extraction
    # - Data validation
    return data.strip().lower()

def evaluate_model(predictions, actuals):
    """
    Evaluate the AI model's predictions against actual values.
    
    Parameters:
    predictions (list): List of predicted values.
    actuals (list): List of actual values.
    
    Returns:
    float: Accuracy score between 0 and 1.
    
    Raises:
    ValueError: If inputs are invalid.
    """
    if not isinstance(predictions, list) or not isinstance(actuals, list):
        raise ValueError("Predictions and actuals must be lists.")
    
    if len(predictions) != len(actuals):
        raise ValueError("Predictions and actuals must have the same length.")
    
    if len(predictions) == 0:
        raise ValueError("Cannot evaluate with empty lists.")
    
    # Calculate accuracy
    accuracy = sum(p == a for p, a in zip(predictions, actuals)) / len(actuals)
    return accuracy
