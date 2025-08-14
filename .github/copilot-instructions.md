# Project Nightingale - GitHub Copilot Instructions

Project Nightingale is a Python 3.9+ health monitoring and prediction system using wearable data and machine learning. It includes CLI and GUI applications, AI/ML modules, and comprehensive testing infrastructure.

**ALWAYS follow these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the information here.**

## Quick Setup & Validation

Bootstrap, build, and test the repository:
- `pip install -r requirements.txt` -- takes ~36 seconds
- `pip install -r requirements-dev.txt` -- takes ~5 seconds  
- **CRITICAL**: Always use `PYTHONPATH=. python` to run Python files - the project requires this for proper module imports
- Test CLI: `PYTHONPATH=. python src/main.py` -- runs in <0.1 seconds
- Run tests: `PYTHONPATH=. pytest tests/ --ignore=tests/test_gui_integration.py --ignore=tests/test_gui_integration_v2.py` -- takes <1 second
- Format code: `black src/ scripts/ --line-length=88` -- takes <1 second
- Lint code: `flake8 src/ scripts/ --max-line-length=88 --extend-ignore=E203` -- takes <1 second

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
- Requires tkinter: `sudo apt-get install python3-tk` (if not available)
- Import test: `PYTHONPATH=. python -c "from gui.main_gui import Application; print('GUI import successful')"`
- Cannot be fully tested in headless environments
- Uses tkinter for the interface

**AI/ML Modules**:
- `scripts/ai_model.py` - Core AI functionality
- `scripts/ai_utilities.py` - Data preprocessing and evaluation utilities
- Test utilities: `PYTHONPATH=. python -c "from scripts.ai_utilities import preprocess_data, evaluate_model; print(preprocess_data('  TEST  '), evaluate_model([1,0,1], [1,1,0]))"`

### Testing
- **Use pytest**: `PYTHONPATH=. pytest tests/` for all tests
- **Skip GUI tests in headless**: Add `--ignore=tests/test_gui_integration.py --ignore=tests/test_gui_integration_v2.py`
- **Expected results**: 88-90 tests pass, 0-2 may fail due to version differences (not critical)
- Test time: <1 second for full suite
- **NEVER CANCEL** tests - they complete very quickly

### Code Quality  
- **Format code**: `black src/ scripts/ --line-length=88`
- **Lint code**: `flake8 src/ scripts/ --max-line-length=88 --extend-ignore=E203`
- **ALWAYS** run both before committing - CI will fail otherwise
- Some flake8 warnings expected in versioned files (not critical)
- Code formatting time: <1 second

## Validation Scenarios

**ALWAYS run this complete validation after making changes:**
1. **CLI functionality**: `PYTHONPATH=. python src/main.py` should output AI processing results with logging
2. **AI utilities**: `PYTHONPATH=. python -c "from scripts.ai_utilities import preprocess_data; print(preprocess_data('  TEST DATA  '))"` should output "test data"
3. **GUI import**: `PYTHONPATH=. python -c "from gui.main_gui import Application; print('Success')"` should complete without errors
4. **Tests pass**: Run pytest command above - should have 88+ passing tests
5. **Code quality**: Run black and flake8 commands above - formatting should complete successfully

## Known Issues & Workarounds

**Import Errors**: If you get "ModuleNotFoundError: No module named 'scripts'" - you forgot `PYTHONPATH=.`

**GUI Tests Fail**: GUI integration tests fail in headless environments - this is expected, ignore with `--ignore` flags

**Flake8 Style Issues**: Many versioned files have style violations - these don't break functionality

**JavaScript File**: `project_nightingale.js` has syntax errors - not critical for Python application

**Flask Not Implemented**: Flask is in requirements but no web server implemented yet

**Database Files**: SQLite database `project_nightingale.db` exists - connection code in some updated main files

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

- **Dependency installation**: 40 seconds total
- **CLI application run**: <0.1 seconds  
- **Test suite**: <1 second
- **Code formatting**: <1 second
- **Linting**: <1 second
- **Validation scenario**: <5 seconds total

All operations in this project are very fast. There are no long build processes or compilation steps.

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
2. Format: `black src/ scripts/ --line-length=88`
3. Lint: `flake8 src/ scripts/ --max-line-length=88 --extend-ignore=E203`
4. Test: `PYTHONPATH=. pytest tests/ --ignore=tests/test_gui_integration.py --ignore=tests/test_gui_integration_v2.py`