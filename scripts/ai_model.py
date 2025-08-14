# AI model implementation for Project Nightingale

def simple_ai_model(input_data):
    """
    A simple AI model that processes input data and returns a result.
    
    Parameters:
    input_data (str): The input data to be processed.
    
    Returns:
    str: A message indicating the processed data.
    
    Raises:
    ValueError: If input_data is not a string.
    """
    if not isinstance(input_data, str):
        raise ValueError("Input data must be a string.")
    
    if not input_data.strip():
        raise ValueError("Input data cannot be empty.")
    
    # Placeholder for AI logic - in a real implementation, this would
    # contain actual machine learning model processing
    processed_data = f"Processed data: {input_data.strip()}"
    return processed_data
