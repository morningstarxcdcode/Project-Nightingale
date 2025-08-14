# Project Nightingale - GitHub Copilot Instructions

Project Nightingale is a Python 3.9+ health monitoring and prediction system using wearable data and machine learning. It includes CLI and GUI applications, AI/ML modules, and comprehensive testing infrastructure.

**ALWAYS follow these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the information here.**

## Quick Setup & Validation

### Essential Setup (Required)
Bootstrap, build, and test the repository:
```bash
# Core dependencies (takes ~40 seconds)
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Development tools (takes ~10 seconds)
pip install black flake8

# GUI support (optional, for environments with display)
sudo apt-get install python3-tk  # May not be available in all environments
```

### **CRITICAL**: Python Execution Requirements
- **ALWAYS** use `PYTHONPATH=. python` to run Python files - the project requires this for proper module imports
- **NEVER** run Python files without `PYTHONPATH=.` - imports will fail

### Quick Validation Commands
```bash
# Test CLI (runs in <1 second)
PYTHONPATH=. python src/main.py

# Run tests (takes ~1 second, 88/90 pass expected)
PYTHONPATH=. pytest tests/ --ignore=tests/test_gui_integration.py --ignore=tests/test_gui_integration_v2.py

# Format code (takes <1 second)
black src/ scripts/ --line-length=88

# Lint code (takes <1 second, warnings expected)
flake8 src/ scripts/ --max-line-length=88 --extend-ignore=E203
```

## Working Effectively

### Python Environment
- Python 3.12.3 available (compatible with 3.9+ requirement)
- Use `pip` for package management
- **NEVER** run Python files without `PYTHONPATH=.` - imports will fail
- All operations are fast (<1 minute) - no long build times to worry about

### Core Applications
**CLI Application** (`src/main.py`):
- Run with: `PYTHONPATH=. python src/main.py`
- Produces AI processing output and logging information
- Uses AI model from `scripts/ai_model.py`
- Import path: `from scripts.ai_model import simple_ai_model`

**GUI Application** (`gui/main_gui.py`):  
- Requires tkinter: `sudo apt-get install python3-tk` (may not be available in headless environments)
- Import test: `PYTHONPATH=. python -c "from gui.main_gui import Application; print('GUI import successful')"`
- **Note**: Cannot be fully tested in headless environments - expect "ModuleNotFoundError: No module named 'tkinter'" in such cases
- Uses tkinter for the interface

**AI/ML Modules**:
- `scripts/ai_model.py` - Core AI functionality
- `scripts/ai_utilities.py` - Data preprocessing and evaluation utilities
- Test utilities: `PYTHONPATH=. python -c "from scripts.ai_utilities import preprocess_data, evaluate_model; print(preprocess_data('  TEST  '), evaluate_model([1,0,1], [1,1,0]))"`

### Testing
- **Use pytest**: `PYTHONPATH=. pytest tests/` for all tests
- **Skip GUI tests in headless**: Add `--ignore=tests/test_gui_integration.py --ignore=tests/test_gui_integration_v2.py`
- **Expected results**: 88/90 tests pass, 2 specific tests fail due to function return type issues (not critical)
- **Failing tests**: `tests/test_ai_updated_v2.py` and `tests/test_main_updated_v2.py` - expect "TypeError: argument of type 'NoneType' is not iterable"
- Test time: <1 second for full suite
- **NEVER CANCEL** tests - they complete very quickly

### Code Quality  
- **Format code**: `black src/ scripts/ --line-length=88`
- **Lint code**: `flake8 src/ scripts/ --max-line-length=88 --extend-ignore=E203`
- **IMPORTANT**: Many flake8 warnings are expected in versioned files (F401 unused imports, F841 unused variables, F821 undefined names)
- **These warnings don't break functionality** - focus on new code being clean
- **ALWAYS** run both before committing - CI will fail otherwise
- Code formatting time: <1 second

## Validation Scenarios

**ALWAYS run this complete validation after making changes:**

### Core Functionality Validation
```bash
# 1. CLI functionality - should output AI processing results with logging
PYTHONPATH=. python src/main.py
# Expected output: 
# INFO:root:Starting the main application...
# INFO:root:AI Result: Processed data: Sample input for AI model

# 2. AI utilities - should output processed data and accuracy score
PYTHONPATH=. python -c "from scripts.ai_utilities import preprocess_data, evaluate_model; print(preprocess_data('  TEST DATA  '), evaluate_model([1,0,1], [1,1,0]))"
# Expected output: test data 0.3333333333333333

# 3. GUI import (skip if in headless environment)
PYTHONPATH=. python -c "from gui.main_gui import Application; print('GUI import successful')"
# Expected: Success message OR "ModuleNotFoundError: No module named 'tkinter'" (acceptable in headless)

# 4. Tests - should have 88 passing, 2 failing
PYTHONPATH=. pytest tests/ --ignore=tests/test_gui_integration.py --ignore=tests/test_gui_integration_v2.py
# Expected: "2 failed, 88 passed"

# 5. Code quality - formatting and linting
black src/ scripts/ --line-length=88  # Should show "All done! ✨ 🍰 ✨"
flake8 src/ scripts/ --max-line-length=88 --extend-ignore=E203  # Warnings expected, not errors
```

### Quick Environment Check
```bash
# Verify all required tools are available
python --version          # Should be 3.9+
pip show pytest black flake8  # Should show package info for all three
```

## Known Issues & Workarounds

### Import Errors
**Issue**: "ModuleNotFoundError: No module named 'scripts'"  
**Solution**: You forgot `PYTHONPATH=.` - always prefix Python commands with this

### GUI Issues
**Issue**: "ModuleNotFoundError: No module named 'tkinter'"  
**Solution**: This is expected in headless environments. GUI tests will fail in such environments - ignore with `--ignore` flags

### Development Tools Missing
**Issue**: "bash: black: command not found" or "bash: flake8: command not found"  
**Solution**: Install development tools with `pip install black flake8`

### Code Quality Warnings
**Issue**: Many flake8 warnings (F401, F841, F821) in existing files  
**Explanation**: These are expected in versioned files from iterative development. Focus on keeping new code clean - these warnings don't break functionality

### Test Failures
**Issue**: 2 tests consistently fail with "TypeError: argument of type 'NoneType' is not iterable"  
**Explanation**: Tests `test_ai_updated_v2.py` and `test_main_updated_v2.py` have return type issues. This is expected and not critical

### JavaScript Syntax Errors
**Issue**: `project_nightingale.js` has syntax errors  
**Explanation**: Not critical for Python application - this file is not actively used

### Flask Not Implemented
**Issue**: Flask is in requirements but no web server exists  
**Explanation**: Flask dependency exists for future development - no current web interface implemented

### Database Connection
**Issue**: SQLite database `project_nightingale.db` exists but connection handling varies  
**Explanation**: Some updated main files include database connection code - this is normal for the iterative development history

## Repository Structure

### Key Directories:
```
src/                    # Main CLI application (use main.py)
gui/                    # GUI applications (use main_gui.py)  
scripts/                # AI/ML modules and utilities
tests/                  # Test suite (many versioned files)
requirements.txt        # Core Python dependencies
requirements-dev.txt    # Development dependencies (pytest)
.github/workflows/      # CodeQL security scanning
```

### Important Files:
- `src/main.py` - Main CLI application entry point
- `gui/main_gui.py` - Main GUI application entry point
- `scripts/ai_model.py` - Core AI model implementation
- `scripts/ai_utilities.py` - Data preprocessing and evaluation
- `tests/test_ai.py` - Primary test file
- `project_nightingale.db` - SQLite database file

### Versioned Files Note:
Many files have version suffixes (e.g., `main_updated_v2.py`, `test_ai_updated_v85.py`) indicating iterative development. Always use the base filenames (`main.py`, `test_ai.py`) unless specifically working with a particular version.

## Time Expectations

- **Dependency installation**: ~40 seconds total (requirements.txt + requirements-dev.txt)
- **Development tools installation**: ~10 seconds (black + flake8)
- **CLI application run**: <1 second  
- **Test suite**: <1 second (88 pass, 2 fail expected)
- **Code formatting**: <1 second
- **Linting**: <1 second (warnings expected, not errors)
- **Complete validation scenario**: <5 seconds total

All operations in this project are very fast. There are no long build processes or compilation steps.

## Troubleshooting

### Environment Setup Issues
1. **If pip install fails**: Check Python version (needs 3.9+) and internet connectivity
2. **If imports fail**: Always use `PYTHONPATH=.` prefix for Python commands
3. **If GUI tests fail**: Install tkinter with `sudo apt-get install python3-tk` or skip GUI testing in headless environments

### Code Quality Issues
1. **If black not found**: Run `pip install black flake8` first
2. **If flake8 shows many warnings**: This is expected in versioned files - focus on your new code
3. **If tests fail beyond expected 2**: Check that you're using correct pytest command with `--ignore` flags

### Development Workflow Issues
1. **If changes don't take effect**: Ensure you're running the correct file (use base names like `main.py`, not versioned files)
2. **If database errors occur**: Check that `project_nightingale.db` exists in project root
3. **If AI utilities fail**: Verify numpy, pandas, scikit-learn are properly installed from requirements.txt

## Common Development Tasks

**Adding new AI functionality**: 
- Modify `scripts/ai_model.py` or `scripts/ai_utilities.py`
- Test with CLI: `PYTHONPATH=. python src/main.py`
- Add tests in `tests/test_ai.py`
- Run validation scenario

**GUI changes**:
- Modify `gui/main_gui.py`
- Test import: `PYTHONPATH=. python -c "from gui.main_gui import Application"`
- Cannot fully test GUI interaction in headless environments

**Before committing any changes**:
1. Run complete validation scenario above
2. Install tools if needed: `pip install black flake8`
3. Format: `black src/ scripts/ --line-length=88`
4. Lint: `flake8 src/ scripts/ --max-line-length=88 --extend-ignore=E203` (warnings expected)
5. Test: `PYTHONPATH=. pytest tests/ --ignore=tests/test_gui_integration.py --ignore=tests/test_gui_integration_v2.py`

### Quick Development Commands
```bash
# Complete setup from scratch
pip install -r requirements.txt -r requirements-dev.txt && pip install black flake8

# Full validation pipeline  
PYTHONPATH=. python src/main.py && \
PYTHONPATH=. pytest tests/ --ignore=tests/test_gui_integration.py --ignore=tests/test_gui_integration_v2.py && \
black src/ scripts/ --line-length=88 && \
flake8 src/ scripts/ --max-line-length=88 --extend-ignore=E203

# Test AI utilities quickly
PYTHONPATH=. python -c "from scripts.ai_utilities import preprocess_data, evaluate_model; print('AI utilities working:', preprocess_data('  TEST  '), evaluate_model([1,0,1], [1,1,0]))"
```