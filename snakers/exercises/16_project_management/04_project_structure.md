# Python Project Structure

Learn best practices for organizing Python projects.

## Exercise: Creating a Well-Structured Python Project

### Part 1: Basic Project Structure

Create a project with this structure:

```
my_project/
│
├── my_package/
│   ├── __init__.py
│   ├── core.py
│   ├── helpers.py
│   └── subpackage/
│       ├── __init__.py
│       └── module.py
│
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_helpers.py
│
├── docs/
│   ├── index.md
│   └── usage.md
│
├── scripts/
│   └── run_analysis.py
│
├── .gitignore
├── README.md
├── setup.py
├── requirements.txt
└── LICENSE
```

### Part 2: Creating Package Files

Create a minimal `setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "pandas>=1.2.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of the package",
    keywords="sample, package, example",
    url="https://github.com/yourusername/my_package",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
)
```

### Part 3: Creating the Package Code

Create a basic module in `my_package/core.py`:

```python
"""Core functionality for my_package."""

def analyze_data(data):
    """
    Analyze the given data.
    
    Args:
        data: The data to analyze
        
    Returns:
        Analysis results
    """
    # Placeholder for actual implementation
    return {"status": "success", "result": f"Analyzed {len(data)} items"}
```

### Part 4: Creating Tests

Create a test file in `tests/test_core.py`:

```python
"""Tests for the core module."""

import unittest
from my_package.core import analyze_data

class TestCore(unittest.TestCase):
    def test_analyze_data(self):
        data = [1, 2, 3, 4, 5]
        result = analyze_data(data)
        
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"], "Analyzed 5 items")

if __name__ == "__main__":
    unittest.main()
```

### Part 5: Creating Documentation

Create a basic README.md:

```markdown
# My Package

A short description of what the package does.

## Installation

```bash
pip install my_package
```

## Usage

```python
from my_package.core import analyze_data

data = [1, 2, 3, 4, 5]
result = analyze_data(data)
print(result)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

### Part 6: Making the Package Installable

Install your package in development mode:

```bash
pip install -e .
```

## Questions to Answer

1. What is the purpose of the `__init__.py` file in Python packages?
2. Why separate code into multiple modules and packages?
3. What's the difference between a module and a package?
4. What are the benefits of making your project installable with `setup.py`?
5. How does the project structure help with maintainability?

## Challenge

Refactor the project to use a modern Python project structure with:
1. pyproject.toml instead of setup.py
2. src-layout (moving package code into a src directory)
3. Add type hints to all functions
4. Add proper docstrings following a standard format (Google, NumPy, or reStructuredText)
