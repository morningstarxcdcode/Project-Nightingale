# Utility functions for AI in Project Nightingale

def preprocess_data(data):
    """
    Preprocess the input data for the AI model.
    
    Parameters:
    data (str): The input data to be preprocessed.

    Returns:
    str: The preprocessed data.
    """
    if not isinstance(data, str):
        raise ValueError("Input data must be a string.")
    
    # Placeholder for preprocessing logic
    return data.strip().lower()

def evaluate_model(predictions, actuals):
    """
    Evaluate the AI model's predictions against actual values.
    
    Parameters:
    predictions (list): The predicted values from the AI model.
    actuals (list): The actual values to compare against.

    Returns:
    float: The accuracy of the predictions.
    """
    if len(predictions) != len(actuals):
        raise ValueError("Predictions and actuals must have the same length.")
    
    # Placeholder for evaluation logic
    accuracy = sum(p == a for p, a in zip(predictions, actuals)) / len(actuals)
    return accuracy
