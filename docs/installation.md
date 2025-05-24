# Installation Guide

## Prerequisites

Before installing Balochi NLP, ensure you have:
- Python 3.8 or higher
- pip (Python package installer)
- Git (for development installation)

## Installation Methods

### 1. Regular Installation (for users)

```bash
pip install balochi-nlp
```

### 2. Development Installation (for contributors)

```bash
# Clone the repository
git clone https://github.com/yourusername/balochi-nlp.git
cd balochi-nlp

# Create and activate virtual environment
## Windows
python -m venv venv
.\venv\Scripts\activate

## macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Install in development mode
pip install -e .
```

### 3. Installing Optional Dependencies

For development and testing:
```bash
pip install -e ".[dev]"
```

## Verifying Installation

```python
# Open Python interpreter
python

# Try importing the package
>>> from balochi_nlp.preprocessing import BalochiTextCleaner
>>> cleaner = BalochiTextCleaner()
```

If no errors occur, the installation was successful.

## Common Issues and Solutions

### Windows-Specific Issues

1. **Command not found**
   - Ensure Python is added to PATH
   - Try using `py` instead of `python`

2. **PowerShell execution policy**
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

### Unix-Specific Issues

1. **Permission errors**
   ```bash
   sudo pip install balochi-nlp
   ```

2. **Python version conflicts**
   - Use `python3` explicitly
   - Consider using `pyenv` for version management

## Uninstallation

To remove the package:
```bash
pip uninstall balochi-nlp
``` 