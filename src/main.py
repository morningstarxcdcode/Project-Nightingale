# Main application file for Project Nightingale

from scripts.ai_model import simple_ai_model
from scripts.ai_utilities import preprocess_data, evaluate_model
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)


def main():
    input_data = "Sample input for AI model"
    result = simple_ai_model(input_data)

    # Log the result
    logging.info(f"AI Result: {result}")

    return f"Welcome to Project Nightingale! AI Result: {result}"


if __name__ == "__main__":
    logging.info("Starting the main application...")
    main()
