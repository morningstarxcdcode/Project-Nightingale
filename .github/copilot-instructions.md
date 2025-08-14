# Project Nightingale - GitHub Copilot Instructions

<tool_calling>
You have the capability to call multiple tools in a single response. For maximum efficiency, whenever you need to perform multiple independent operations, ALWAYS invoke all relevant tools simultaneously rather than sequentially. Especially when exploring repository, reading files, viewing directories, validating changes or replying to comments.
</tool_calling>

## Project Overview

Project Nightingale is an AI-powered cybersecurity analysis tool with a comprehensive GUI interface and robust testing framework. The project combines machine learning capabilities with user-friendly interfaces for advanced security analysis.

## Architecture

### Core Components:
- **src/**: Main application source code and entry points
- **gui/**: Tkinter-based graphical user interfaces with AI integration
- **scripts/**: AI models, utilities, and networking functionality
- **tests/**: Comprehensive test suite including unit, integration, and GUI tests

### Key Features:
- AI model integration for data processing
- Interactive GUI applications
- RESTful API endpoints via Flask
- Comprehensive testing framework
- CodeQL security analysis
- Multi-language support

## Development Guidelines

### Code Style:
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for all functions and classes
- Maintain consistent error handling

### Testing Requirements:
- All new functionality must include tests
- Run full test suite before committing: `python -m pytest tests/ -v`
- GUI tests should work without requiring display
- Integration tests should cover complete workflows

### Project Structure:
```
Project-Nightingale/
├── src/main.py              # Main application entry point
├── gui/                     # GUI applications
│   ├── main_gui.py          # Basic GUI with AI integration
│   └── main_gui_with_ai_integration.py  # Advanced GUI features
├── scripts/                 # Core functionality
│   ├── ai_model.py          # AI model implementation
│   ├── ai_utilities.py      # Utility functions
│   └── networking.py        # Network/API utilities
├── tests/                   # Test suite
│   ├── test_ai.py           # AI model tests
│   ├── test_api.py          # API endpoint tests
│   ├── test_integration.py  # Integration tests
│   └── test_gui_integration.py  # GUI integration tests
└── requirements.txt         # Python dependencies
```

## Common Tasks

### Running the Application:
```bash
# Main CLI application
python src/main.py

# GUI application
python gui/main_gui.py

# GUI with AI integration
python gui/main_gui_with_ai_integration.py
```

### Testing:
```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_gui_integration.py -v

# Run with coverage
python -m pytest tests/ --cov=. --cov-report=html
```

### Development Workflow:
1. Create feature branch from main
2. Implement changes with tests
3. Run full test suite
4. Update documentation if needed
5. Submit pull request

## Dependencies
- **flask**: Web framework for API endpoints
- **pytest**: Testing framework
- **tkinter**: GUI framework (included with Python)
- **requests**: HTTP library for networking

## Security Considerations
- Input validation for all user data
- Secure API endpoint design
- Regular dependency updates
- CodeQL analysis integration

## Contributing
See CONTRIBUTING.md for detailed contribution guidelines including coding standards, testing requirements, and pull request process.