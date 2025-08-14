# Project Nightingale - GitHub Copilot Instructions

Project Nightingale is a Python-based health monitoring and prediction system using wearable data and machine learning. It provides a personalized health analytics platform with GUI interface, REST API, and AI model components.

**ALWAYS reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Environment Setup
- **Python Version**: Use Python 3.9+ (tested with Python 3.12.3)
- **CRITICAL**: Always set PYTHONPATH when running Python commands:
  ```bash
  export PYTHONPATH=/path/to/Project-Nightingale
  ```
- **Repository Structure**:
  - `/src/main.py` - Main application entry point
  - `/scripts/` - AI model and utility scripts  
  - `/gui/` - Tkinter-based GUI applications
  - `/tests/` - pytest test files
  - `/requirements.txt` - Python dependencies (compatible with Python 3.12+)

### Dependencies Installation
- **RECOMMENDED**: Install dependencies using pip from requirements.txt:
  ```bash
  pip3 install -r requirements.txt
  ```
- **ALTERNATIVE**: Install via system packages if pip is not available:
  ```bash
  sudo apt update
  sudo apt install -y python3-tk python3-flask python3-pytest
  ```
- **Manual ML dependencies** (if needed separately):
  ```bash
  pip3 install numpy pandas scikit-learn matplotlib seaborn tensorflow
  ```

### Build and Test Commands
- **Run Main Application** (takes <1 second):
  ```bash
  cd /path/to/Project-Nightingale
  PYTHONPATH=/path/to/Project-Nightingale python3 src/main.py
  ```
- **Run Test Suite** (takes <1 second - NEVER CANCEL, but very fast):
  ```bash
  cd /path/to/Project-Nightingale
  PYTHONPATH=/path/to/Project-Nightingale python3 -m pytest tests/test_ai.py -v
  ```
- **Run Full Test Suite** (takes <1 second - includes 94 tests, 4 expected failures due to GUI/display issues):
  ```bash
  cd /path/to/Project-Nightingale  
  PYTHONPATH=/path/to/Project-Nightingale python3 -m pytest tests/ -v
  ```

### Running the Applications

#### Command Line Application
```bash
cd /path/to/Project-Nightingale
PYTHONPATH=/path/to/Project-Nightingale python3 src/main.py
```
Expected output:
```
INFO:root:Starting the main application...
INFO:root:AI Result: Processed data: Sample input for AI model
```

#### GUI Application  
```bash
cd /path/to/Project-Nightingale
PYTHONPATH=/path/to/Project-Nightingale python3 gui/main_gui.py
```
**NOTE**: GUI requires X11 display. In headless environments, test with import only:
```bash
PYTHONPATH=/path/to/Project-Nightingale python3 -c "import gui.main_gui; print('GUI module loads successfully')"
```

#### REST API Server
Create and run a Flask server based on README examples:
```bash
# Use the API endpoints described in README.md
curl -X GET http://localhost:5000/api/health
curl -X POST -H "Content-Type: application/json" -d '{"data": "your_data_here"}' http://localhost:5000/api/data
```

## Validation and Testing

### Manual Validation Requirements
- **ALWAYS** test these scenarios after making changes:
  1. **Basic functionality**: Run `python3 src/main.py` and verify it outputs AI processing results
  2. **Test suite**: Run `python3 -m pytest tests/test_ai.py -v` and verify 2 tests pass
  3. **Module imports**: Test `import gui.main_gui` succeeds
  4. **API endpoints**: If Flask server implemented, test health and data endpoints with curl

### Expected Test Results
- **Main test file**: 2 tests pass in tests/test_ai.py
- **Full test suite**: 90 tests pass, 4 fail (GUI display issues - expected in headless environments)
- **Test timing**: Complete test suite runs in under 1 second

### Working Components Validation
- ✅ **Core AI Model**: `scripts/ai_model.py` - simple_ai_model() function works
- ✅ **Main Application**: `src/main.py` - runs successfully with proper PYTHONPATH
- ✅ **GUI Module**: `gui/main_gui.py` - imports successfully (needs display to run)
- ✅ **Testing Framework**: pytest works with system packages
- ✅ **Flask Support**: Available via apt packages, API endpoints functional
- ✅ **SQLite Database**: Built-in Python support, project_nightingale.db file exists (empty)

### Common Issues and Solutions

### Dependency Problems
- **Issue**: Need to install dependencies
- **Solution**: Use `pip3 install -r requirements.txt` (recommended) or system packages

### Import Errors
- **Issue**: `ModuleNotFoundError: No module named 'scripts'`
- **Solution**: Always set PYTHONPATH before running Python commands:
  ```bash
  export PYTHONPATH=/path/to/Project-Nightingale
  ```

### GUI Testing
- **Issue**: `_tkinter.TclError: no display name and no $DISPLAY environment variable`
- **Solution**: This is expected in headless environments. Test GUI code with import validation only.

## Development Workflow

### Before Making Changes
1. **Verify working state**:
   ```bash
   PYTHONPATH=/path/to/Project-Nightingale python3 src/main.py
   PYTHONPATH=/path/to/Project-Nightingale python3 -m pytest tests/test_ai.py -v
   ```

### After Making Changes
1. **Test core functionality**: Run main application
2. **Run relevant tests**: Focus on tests/test_ai.py for core changes
3. **Validate imports**: Ensure module imports still work
4. **Check AI model**: Verify `simple_ai_model()` function processes input correctly

### Code Style and Structure
- **Follow PEP 8**: Use standard Python formatting
- **Import Structure**: Add new modules to PYTHONPATH or use relative imports
- **Testing**: Add tests to existing test files or create new ones in `/tests/` directory
- **Documentation**: Update docstrings for any modified functions

## Repository Navigation

### Key Files and Locations
- **Entry Point**: `/src/main.py` - Start here for understanding application flow
- **AI Logic**: `/scripts/ai_model.py` - Core AI processing functions
- **GUI Components**: `/gui/main_gui.py` - Primary GUI application
- **Test Files**: `/tests/test_ai.py` - Main test coverage
- **Configuration**: `/requirements.txt` - Python dependencies (compatible with Python 3.12+)
- **Documentation**: `/README.md`, `/CONTRIBUTING.md` - Project information

### Frequently Used Commands Summary
```bash
# Set environment (ALWAYS required)
export PYTHONPATH=/path/to/Project-Nightingale

# Quick functionality test  
python3 src/main.py

# Run core tests
python3 -m pytest tests/test_ai.py -v

# Test GUI import
python3 -c "import gui.main_gui; print('GUI works')"

# Install working dependencies
pip3 install -r requirements.txt
```

**TIMING EXPECTATIONS**: All commands complete in under 1 second. No long builds or installations required for basic functionality.