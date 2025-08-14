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
- Clean, well-structured codebase
- Comprehensive testing suite
- Both CLI and GUI interfaces

## Installation

### For End Users

1. Clone the repository:

   ```bash
   git clone https://github.com/morningstarxcdcode/Project-Nightingale.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Project-Nightingale
   ```

3. Install the package:

   ```bash
   pip install .
   ```

### For Developers

1. Clone the repository:

   ```bash
   git clone https://github.com/morningstarxcdcode/Project-Nightingale.git
   cd Project-Nightingale
   ```

2. Install in development mode with testing dependencies:

   ```bash
   pip install -e .[dev]
   ```

## Usage

### Command Line Interface

To run the application via command line:

```bash
# If installed via pip
nightingale

# Or directly
python src/main.py
```

### Graphical User Interface

To run the GUI application:

```bash
# If installed via pip (requires tkinter)
nightingale-gui

# Or directly
python gui/main_gui.py
```

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

## Project Structure

```
Project-Nightingale/
├── src/                    # Core application code
│   └── main.py            # Main CLI entry point
├── gui/                   # GUI components
│   └── main_gui.py       # Main GUI application
├── scripts/              # AI models and utilities
│   ├── ai_model.py       # AI model implementation
│   └── ai_utilities.py   # AI utility functions
├── tests/                # Test suite
│   ├── test_ai.py        # AI functionality tests
│   └── test_ai_utilities.py # AI utilities tests
├── docs/                 # Documentation
├── requirements.txt      # Python dependencies
├── setup.py             # Package setup configuration
└── README.md           # This file
```

## Running Tests

To run the tests for this project, you can use `pytest`. Make sure you have installed the development dependencies first.

Run the following command in your terminal:

```bash
pytest tests/
```

For coverage reports:

```bash
pytest tests/ --cov=src --cov=scripts --cov=gui
```

## Development

### Code Quality

The project maintains high code quality through:
- Comprehensive test suite
- Clear documentation
- Modular architecture
- Error handling and validation

### Contributing

We welcome contributions! Please see the `CONTRIBUTING.md` file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
