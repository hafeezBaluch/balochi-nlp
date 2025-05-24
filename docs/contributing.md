# Contributing Guide

Thank you for your interest in contributing to Balochi NLP! This document provides guidelines and instructions for contributing to the project.

## Development Setup

### 1. Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
```bash
git clone https://github.com/your-username/balochi-nlp.git
cd balochi-nlp
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install development dependencies
pip install -e ".[dev]"
```

### 3. Run Tests

```bash
pytest
```

## Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and single-purpose
- Use type hints where possible

Example:
```python
def clean_text(
    text: str,
    remove_numbers: bool = True,
    preserve_special_chars: bool = True
) -> str:
    """Clean and normalize Balochi text.

    Args:
        text: Input text to clean
        remove_numbers: Whether to remove numerical digits
        preserve_special_chars: Whether to preserve Balochi special characters

    Returns:
        Cleaned text string
    """
    # Implementation
```

### Git Workflow

1. Create a new branch for your feature:
```bash
git checkout -b feature-name
```

2. Make your changes and commit:
```bash
git add .
git commit -m "Description of changes"
```

3. Keep your fork up to date:
```bash
git remote add upstream https://github.com/original/balochi-nlp.git
git fetch upstream
git rebase upstream/main
```

4. Push changes and create pull request:
```bash
git push origin feature-name
```

### Pull Request Guidelines

1. **Before Submitting:**
   - Run all tests
   - Update documentation if needed
   - Add tests for new features
   - Follow code style guidelines

2. **PR Description:**
   - Clearly describe the changes
   - Reference any related issues
   - Include before/after examples if relevant

3. **Review Process:**
   - Address review comments
   - Keep PR focused on single feature/fix
   - Be responsive to feedback

## Testing

### Writing Tests

1. **Test Structure:**
```python
def test_feature_name():
    """Test description."""
    # Arrange
    input_data = "test input"
    expected = "expected output"
    
    # Act
    result = function_to_test(input_data)
    
    # Assert
    assert result == expected
```

2. **Test Categories:**
   - Unit tests for individual functions
   - Integration tests for component interaction
   - Edge cases and error conditions

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_cleaner.py

# Run with coverage
pytest --cov=balochi_nlp

# Generate coverage report
pytest --cov=balochi_nlp --cov-report=html
```

## Documentation

### Writing Documentation

1. **Docstrings:**
   - Use Google style docstrings
   - Include types, parameters, returns
   - Add examples where helpful

2. **README Updates:**
   - Keep installation instructions current
   - Update feature list
   - Add new examples

3. **API Documentation:**
   - Document all public interfaces
   - Include usage examples
   - Note any breaking changes

## Release Process

1. **Version Bump:**
   - Update version in setup.py
   - Update CHANGELOG.md
   - Create release notes

2. **Testing:**
   - Run full test suite
   - Test installation from clean environment
   - Verify documentation accuracy

3. **Release:**
   - Tag release in git
   - Build and upload to PyPI
   - Update documentation

## Getting Help

- Open an issue for bugs
- Use discussions for questions
- Join our community chat
- Contact maintainers directly

## Code of Conduct

Please note that this project follows a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code. 