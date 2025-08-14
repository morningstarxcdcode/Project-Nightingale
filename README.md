# Project-Nightingale

Project Nightingale is designed to be the vigilant guardian of your codebase, ensuring its health, maintainability, and overall quality, allowing your development process to sing with efficiency and clarity.

## Python Version

This project is developed using Python 3.9+. Ensure you have the correct version installed.

## Motivation

The goal of Project Nightingale is to provide a personalized health monitoring and prediction system using wearable data and machine learning. This project aims to empower users to take control of their health through data-driven insights.

## Features

- Personalized health monitoring
- Predictive analytics using machine learning
- User-friendly interface for data visualization

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/morningstarxcdcode/Project-Nightingale.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Project-Nightingale
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   **Note**: If you encounter dependency issues, you can install the minimal required packages:

   ```bash
   pip install flask pytest
   ```

   The core functionality will work with just these packages, and you can add additional ML libraries as needed.

## Usage

### Running the Core Application

To run the main application, execute:

```bash
python src/main.py
```

### Running the Flask API Server

To start the API server, execute:

```bash
python src/app.py
```

The API will be available at `http://localhost:5000` with the following endpoints:

- `GET /` - API information and available endpoints
- `GET /api/health` - Health check endpoint
- `POST /api/data` - Process data through the AI model
- `POST /api/predict` - Make predictions using the AI model

### Running the GUI Application

To start the graphical user interface, execute:

```bash
python gui/main_gui.py
```

**Note**: The GUI requires tkinter, which is typically included with Python installations. If running in a headless environment or if tkinter is not available, you can use the Flask API or command-line interface instead.

### Sample API Calls

You can interact with the API using tools like `curl` or Python's `requests` library. Here are some examples:

- **Get Health Data**:

  ```bash
  curl -X GET http://localhost:5000/api/health
  ```

- **Post New Data**:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"data": "your_data_here"}' http://localhost:5000/api/data
  ```

- **Make Predictions**:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"input": "prediction_input"}' http://localhost:5000/api/predict
  ```

## Running Tests

To run the tests for this project, you can use `pytest`. Make sure you have installed the required dependencies first.

Run the following command in your terminal:

```bash
pytest tests/
```

## Visuals

![Architecture Overview](path_to_architecture_diagram.png)

## Contribution

We welcome contributions! Please see the `CONTRIBUTING.md` file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
