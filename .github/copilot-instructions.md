# Copilot Instructions for Project Nightingale

## Repository Overview

Project Nightingale is a production-ready health monitoring and prediction system using wearable data and machine learning. The repository follows enterprise-grade Python development practices with comprehensive testing, type safety, and professional code organization.

## Project Structure

- **`src/`** - Main application entry points and core business logic
- **`scripts/`** - AI models, utilities, configuration, and supporting modules
- **`gui/`** - Modern GUI interface components using tkinter with enhanced UX
- **`tests/`** - Comprehensive test suite with 75+ tests and extensive coverage
- **`docs/`** - Documentation and database samples
- **`.github/`** - CI/CD workflows, quality checks, and repository configuration

## Code Review Focus Areas

When reviewing code changes, please pay attention to:

### 1. Python Best Practices & Type Safety
- **Type Hints**: All functions must have complete type annotations (`-> ReturnType`)
- **Docstrings**: Google-style docstrings with Args, Returns, Raises, and Examples
- **PEP 8 Compliance**: Enforced via Black formatter and flake8 linting
- **Error Handling**: Custom exception classes with proper inheritance and chaining
- **Input Validation**: Comprehensive validation with meaningful error messages
- **Code Organization**: Clean imports, proper module structure, no circular dependencies

### 2. AI/ML Components Excellence
- **Model Validation**: Input/output validation, type checking, edge case handling
- **Data Preprocessing**: Robust preprocessing pipeline with Unicode support
- **Performance Metrics**: Comprehensive evaluation with accuracy, MAE, MSE, RMSE
- **Memory Usage**: Efficient algorithms, proper cleanup, thread safety
- **Logging**: Detailed debug/info logging for model operations
- **Error Recovery**: Graceful handling of model failures with informative messages

### 3. GUI Components & User Experience
- **Modern Interface**: Professional tkinter GUI with ttk styling and responsive design
- **Event Handling**: Robust input validation, keyboard shortcuts, error feedback
- **User Feedback**: Progress indicators, status updates, clear error messages
- **Accessibility**: Keyboard navigation, clear visual hierarchy, responsive layout
- **Configuration**: User preferences, window state management, theme support
- **Performance**: Asynchronous operations, non-blocking UI, smooth interactions

### 4. Testing Excellence & Quality Assurance
- **Test Coverage**: Minimum 80% coverage with meaningful assertions
- **Test Types**: Unit tests, integration tests, performance tests, edge cases
- **Parametrized Testing**: Use pytest parametrize for comprehensive test coverage
- **Mock Usage**: Proper mocking of external dependencies and system calls
- **Test Organization**: Clear test structure, descriptive names, good documentation
- **Performance Testing**: Thread safety, memory usage, benchmark validation

### 5. Security & Robustness
- **Input Sanitization**: All user inputs validated and sanitized
- **Data Protection**: Secure handling of sensitive health data
- **Exception Safety**: Proper exception handling without information leakage
- **Dependency Security**: Regular security audits with safety and bandit
- **Configuration Security**: Secure defaults, environment variable validation
- **Database Security**: Parameterized queries, connection management, timeouts

### 6. Performance & Scalability
- **Algorithm Efficiency**: O(n) complexity analysis, optimization opportunities
- **Memory Management**: Proper cleanup, garbage collection, memory profiling
- **Caching Strategy**: Intelligent caching of expensive operations
- **Database Optimization**: Efficient queries, connection pooling, indexing
- **Concurrent Processing**: Thread safety, async operations where beneficial
- **Resource Monitoring**: Memory usage tracking, performance benchmarks

### 7. Configuration & DevOps
- **Configuration Management**: Centralized config with environment overrides
- **Environment Support**: Development, testing, production configurations
- **CI/CD Pipeline**: Automated testing, linting, security checks, deployment
- **Code Quality**: Black formatting, isort imports, mypy type checking, flake8 linting
- **Documentation**: Comprehensive README, API docs, deployment guides
- **Monitoring**: Application logging, error tracking, performance metrics

## Advanced Quality Standards

### Code Architecture
- **SOLID Principles**: Single responsibility, open/closed, dependency inversion
- **Design Patterns**: Appropriate use of patterns (Factory, Observer, Strategy)
- **Modularity**: Clear separation of concerns, minimal coupling
- **Extensibility**: Easy to add new features without breaking existing functionality
- **Maintainability**: Self-documenting code, clear abstractions, good naming

### Testing Strategy
- **Test Pyramid**: Unit tests (majority), integration tests, e2e tests
- **Edge Cases**: Boundary conditions, error scenarios, edge inputs
- **Performance Tests**: Load testing, memory profiling, concurrency testing
- **Security Tests**: Input validation, authentication, authorization
- **Regression Tests**: Prevent regression of fixed bugs

### Error Handling & Logging
- **Custom Exceptions**: Domain-specific exception hierarchy with error codes
- **Logging Levels**: Appropriate use of DEBUG, INFO, WARNING, ERROR, CRITICAL
- **Structured Logging**: Consistent log format with contextual information
- **Error Recovery**: Graceful degradation, fallback mechanisms
- **User Communication**: Clear, actionable error messages for end users

## Key Files and Components

### Core Application Files
- **`src/main.py`** - Enhanced main application with configuration, database, and error handling
- **`scripts/ai_model.py`** - Production-ready AI model with comprehensive validation
- **`scripts/ai_utilities.py`** - Advanced utilities with metrics calculation and performance optimization
- **`scripts/config.py`** - Enterprise configuration management with environment support
- **`scripts/exceptions.py`** - Professional exception hierarchy with error codes

### GUI and Interface
- **`gui/main_gui.py`** - Modern GUI with enhanced UX, progress indicators, and robust error handling

### Testing Infrastructure
- **`tests/test_*.py`** - Comprehensive test suite with 75+ tests covering all functionality
- **`pyproject.toml`** - Complete development configuration for quality tools

### DevOps and Quality
- **`.github/workflows/quality.yml`** - Comprehensive CI/CD pipeline with multi-OS testing
- **`.github/copilot-instructions.md`** - This enhanced review guide

## Dependencies and Requirements

### Production Dependencies
- **Python 3.9+**: Modern Python with type hints and dataclasses
- **Scientific Stack**: numpy, pandas, scikit-learn for ML operations
- **Visualization**: matplotlib, seaborn for data visualization
- **Web Framework**: Flask for API endpoints
- **GUI Framework**: tkinter for cross-platform desktop interface

### Development Dependencies
- **Testing**: pytest, pytest-cov, pytest-mock for comprehensive testing
- **Code Quality**: black, isort, flake8, mypy for code formatting and analysis
- **Security**: bandit, safety for security scanning
- **Documentation**: sphinx for API documentation generation

## Review Priorities & Checklist

### 🔍 Code Quality (High Priority)
- [ ] Type hints present and accurate
- [ ] Docstrings complete with examples
- [ ] Error handling comprehensive
- [ ] Input validation robust
- [ ] Code follows SOLID principles

### 🧪 Testing (High Priority)
- [ ] Tests cover new functionality
- [ ] Edge cases included
- [ ] Performance tests for critical paths
- [ ] Mocks used appropriately
- [ ] Test coverage maintained >80%

### 🚀 Performance (Medium Priority)
- [ ] No obvious performance bottlenecks
- [ ] Memory usage reasonable
- [ ] Database queries optimized
- [ ] Async operations where beneficial
- [ ] Caching strategy appropriate

### 🔒 Security (Medium Priority)
- [ ] Input validation prevents injection
- [ ] Sensitive data handled securely
- [ ] Dependencies have no known vulnerabilities
- [ ] Error messages don't leak information
- [ ] Authentication/authorization appropriate

### 📱 User Experience (Medium Priority)
- [ ] GUI responsive and intuitive
- [ ] Error messages clear and actionable
- [ ] Progress feedback for long operations
- [ ] Keyboard shortcuts available
- [ ] Accessibility considerations

### 📖 Documentation (Low Priority)
- [ ] README updated for new features
- [ ] API documentation current
- [ ] Configuration options documented
- [ ] Deployment guide accurate
- [ ] Changelog updated

## Common Issues to Watch For

### Anti-Patterns
1. **Missing Type Hints** - All public functions must have type annotations
2. **Poor Error Messages** - Errors should be actionable and user-friendly
3. **Hardcoded Values** - Use configuration system for customizable values
4. **Missing Tests** - All new functionality requires corresponding tests
5. **Performance Regressions** - Monitor for O(n²) algorithms or memory leaks

### Best Practices to Enforce
1. **Fail Fast** - Validate inputs early and provide immediate feedback
2. **Defensive Programming** - Assume inputs can be malicious or malformed
3. **Separation of Concerns** - Keep business logic separate from UI and data layers
4. **Configuration Over Code** - Use config files for environment-specific settings
5. **Logging Over Print** - Use proper logging framework with appropriate levels

## Review Workflow

When reviewing PRs, follow this systematic approach:

1. **Architecture Review** - Does the change fit the overall system design?
2. **Code Quality** - Are standards maintained (types, docs, tests)?
3. **Security Assessment** - Are there any security implications?
4. **Performance Impact** - Could this affect system performance?
5. **User Experience** - How does this affect the end user?
6. **Maintainability** - Will this be easy to maintain and extend?

Focus on these areas to provide the most valuable feedback for maintaining the high quality and professional standards of Project Nightingale. The goal is to keep this codebase production-ready, secure, performant, and maintainable for healthcare applications.