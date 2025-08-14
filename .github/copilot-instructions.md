# Project Nightingale - GitHub Copilot Instructions

Project Nightingale is a Python-based health monitoring and prediction system using machine learning and data visualization. It features a Tkinter GUI for user interaction, core AI models for health data processing, and comprehensive test coverage.

**ALWAYS follow these instructions first and only fallback to additional search or bash commands if the information here is incomplete or found to be in error.**

## Working Effectively

### Bootstrap and Environment Setup
- **Python Version**: Requires Python 3.9+. Current environment uses Python 3.12.3.
- **System Dependencies**: Install tkinter for GUI functionality:
  ```bash
  sudo apt-get update && sudo apt-get install -y python3-tk
  ```
- **Python Dependencies**: Install all required packages:
  ```bash
  pip install -r requirements.txt
  pip install -r requirements-dev.txt
  ```
  - Main install takes approximately 35 seconds. NEVER CANCEL.
  - Dev install takes approximately 4 seconds.

### Running the Application
- **CRITICAL**: Always set PYTHONPATH before running any Python modules:
  ```bash
  export PYTHONPATH=/path/to/Project-Nightingale  # Replace with actual project path
  ```
  **Note**: Replace `/path/to/Project-Nightingale` with your actual project directory path (e.g., `/home/runner/work/Project-Nightingale/Project-Nightingale`)
- **Main Application**: 
  ```bash
  PYTHONPATH=/path/to/Project-Nightingale python src/main.py  # Replace with actual path
  ```
  - Executes instantly (<1 second)
  - Processes sample AI model data and outputs results to console
  - Uses logging framework for output

- **GUI Application**:
  ```bash
  PYTHONPATH=/path/to/Project-Nightingale python gui/main_gui_with_ai_integration.py  # Replace with actual path
  ```
  - Requires X11 display for GUI interaction
  - In headless environments, will fail with "no display name and no $DISPLAY environment variable" - this is expected
  - GUI integrates with AI model functionality

### Testing
- **Run All Tests**:
  ```bash
  PYTHONPATH=/path/to/Project-Nightingale python -m pytest tests/ -v  # Replace with actual path
  ```
  - Test suite completes in <1 second for core functionality. NEVER CANCEL.
  - 90+ test files available, many are versioned iterations
  - 4 GUI integration tests will fail in headless environments due to tkinter display requirements - this is expected

- **Run Core Tests Only**:
  ```bash
  PYTHONPATH=/path/to/Project-Nightingale python -m pytest tests/test_ai.py -v  # Replace with actual path
  ```
  - Core AI tests complete in <0.1 seconds

### Validation Scenarios
**ALWAYS manually validate changes using these complete scenarios:**

1. **Core AI Workflow Test**:
   ```bash
   PYTHONPATH=/path/to/Project-Nightingale python -c "
   from scripts.ai_model import simple_ai_model
   from scripts.ai_utilities import preprocess_data, evaluate_model
   
   # Test complete workflow
   test_data = 'Sample Health Data for Processing'
   processed = preprocess_data(test_data)
   result = simple_ai_model(processed)
   print(f'AI Result: {result}')
   
   # Test evaluation
   predictions = ['healthy', 'sick', 'healthy']
   actuals = ['healthy', 'healthy', 'healthy'] 
   accuracy = evaluate_model(predictions, actuals)
   print(f'Model Accuracy: {accuracy:.2f}')
   "
   ```
   Expected output: Shows processed data flow and accuracy calculation

2. **Main Application Integration Test**:
   ```bash
   PYTHONPATH=/path/to/Project-Nightingale python src/main.py
   ```
   Expected output: Console logging showing "AI Result: Processed data: Sample input for AI model"

3. **Import Validation Test**:
   ```bash
   PYTHONPATH=/path/to/Project-Nightingale python -c "
   from src.main import main
   from scripts.ai_model import simple_ai_model
   from scripts.ai_utilities import preprocess_data, evaluate_model
   print('All imports successful')
   "
   ```

## Project Structure

### Key Directories
- **`src/`**: Main application entry points
  - `main.py`: Primary application entry point
  - Multiple versioned main files (main_updated_v*.py)
- **`scripts/`**: Core utility modules
  - `ai_model.py`: AI model implementation
  - `ai_utilities.py`: Data preprocessing and evaluation functions
  - `utilities.py`: General utility functions
  - `networking/`: Network-related functionality
- **`gui/`**: Tkinter GUI applications
  - `main_gui_with_ai_integration.py`: Main GUI with AI functionality
  - Multiple GUI variants and versions
- **`tests/`**: Comprehensive test suite
  - `test_ai.py`: Core AI functionality tests
  - 85+ additional versioned test files
- **`docs/`**: Documentation and feature specifications

### Dependencies
- **Core ML Libraries**: numpy (2.3.2), pandas (2.3.1), scikit-learn (1.7.1)
- **Visualization**: matplotlib (3.10.5), seaborn (0.13.2)
- **Web Framework**: flask (2.3.3) (available but not actively used in current main app)
- **Testing**: pytest (8.4.1)
- **GUI**: tkinter (system package)

### Database
- **SQLite Database**: `project_nightingale.db` (empty file, used for data persistence)

## Build and Deployment
- **No Build Process**: This is a pure Python application with no compilation step
- **No Linting Tools Configured**: flake8, pylint, black, mypy are not currently available
- **CI/CD**: GitHub Actions configured for CodeQL security scanning only (.github/workflows/codeql.yml)

## Common Tasks and Troubleshooting

### Module Import Issues
- **Always set PYTHONPATH**: The most common issue is missing PYTHONPATH configuration
- **Verify working directory**: Ensure you're in the project root directory

### GUI Issues  
- **Headless Environment**: GUI applications will fail without X11 display - this is expected behavior
- **tkinter Missing**: Install with `sudo apt-get install python3-tk`

### Test Failures
- **GUI Integration Tests**: May fail in headless environments - this is expected
- **Database Tests**: Some versioned tests may have different expectations - focus on core tests

### Performance Expectations
- **Dependencies Installation**: ~35 seconds for main requirements, ~4 seconds for dev requirements
- **Application Startup**: Instant (<1 second)
- **Test Execution**: ~0.2 seconds for full test suite (90 pass, 4 GUI tests fail in headless), <0.1 seconds for core AI tests
- **NEVER CANCEL**: While operations are fast, always wait for completion

## Quick Reference Commands

```bash
# Setup (run once)
sudo apt-get install -y python3-tk
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Set environment (run in each session)
export PYTHONPATH=/path/to/Project-Nightingale  # Replace with actual project path

# Run application
python src/main.py

# Run tests
python -m pytest tests/test_ai.py -v

# Validate AI workflow
python -c "from scripts.ai_model import simple_ai_model; print(simple_ai_model('test'))"
```

## Development Workflow
1. **Always set PYTHONPATH** before any Python operations
2. **Test core functionality** with `python src/main.py`
3. **Run relevant tests** with `python -m pytest tests/test_ai.py -v`
4. **Validate AI workflow** using the manual validation scenarios above
5. **Test GUI functionality** if making GUI changes (may require display)

This project prioritizes rapid development iteration with comprehensive testing. All operations complete quickly, enabling fast feedback cycles during development.