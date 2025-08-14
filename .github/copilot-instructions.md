# Copilot Instructions for Project Nightingale

## Repository Overview

Project Nightingale is a health monitoring and prediction system using wearable data and machine learning. The repository follows a clean Python package structure with proper separation of concerns.

## Project Structure

- **`src/`** - Main application entry points and core logic
- **`scripts/`** - AI models, utilities, and networking modules
- **`gui/`** - GUI interface components using tkinter
- **`tests/`** - Comprehensive test suite with pytest
- **`docs/`** - Documentation and database samples
- **`.github/`** - CI/CD workflows and repository configuration

## Code Review Focus Areas

When reviewing code changes, please pay attention to:

### 1. Python Best Practices
- Proper use of type hints and docstrings
- PEP 8 compliance and code formatting
- Error handling with appropriate exceptions
- Input validation and sanitization

### 2. AI/ML Components
- Model validation and testing
- Data preprocessing and feature engineering
- Performance metrics and evaluation
- Memory usage and computational efficiency

### 3. GUI Components
- User experience and interface design
- Event handling and user input validation
- Error messages and user feedback
- Accessibility considerations

### 4. Testing Coverage
- Unit tests for all new functionality
- Integration tests for component interactions
- Mock usage for external dependencies
- Test data management and cleanup

### 5. Security Considerations
- Input sanitization and validation
- Secure data handling practices
- Protection against common vulnerabilities
- Proper error message handling (no sensitive data exposure)

### 6. Performance and Scalability
- Memory usage optimization
- Algorithmic efficiency
- Database query optimization
- Resource cleanup and management

## Key Files to Review

- **`src/main.py`** - Main application entry point
- **`scripts/ai_model.py`** - Core AI/ML functionality
- **`scripts/ai_utilities.py`** - AI utility functions
- **`gui/main_gui.py`** - Main GUI application
- **`tests/`** - All test files for functionality verification

## Dependencies and Requirements

- Python 3.9+ compatibility
- Standard scientific computing stack (numpy, pandas, scikit-learn)
- GUI framework (tkinter)
- Testing framework (pytest)

## Common Issues to Watch For

1. **Import Structure** - Ensure proper relative imports and package structure
2. **Code Duplication** - Look for repeated code that could be refactored
3. **Error Handling** - Check for proper exception handling and user feedback
4. **Documentation** - Verify docstrings and inline comments are helpful
5. **Test Coverage** - Ensure new features have corresponding tests

## Review Priorities

1. **Functionality** - Does the code work as intended?
2. **Maintainability** - Is the code clean and well-organized?
3. **Performance** - Are there any obvious performance issues?
4. **Security** - Are there potential security vulnerabilities?
5. **Testing** - Is the code properly tested?

When reviewing PRs, focus on these areas to provide the most valuable feedback for maintaining code quality and project goals.