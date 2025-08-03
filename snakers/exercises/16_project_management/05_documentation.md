# Documentation in Python Projects

Learn how to create effective documentation for your Python code and projects.

## Exercise: Creating Comprehensive Documentation

### Part 1: Docstring Formats

Write a function with different docstring formats:

Google Style:
```python
def calculate_statistics(numbers):
    """
    Calculate basic statistics from a list of numbers.
    
    Args:
        numbers (list): A list of numeric values
        
    Returns:
        dict: A dictionary containing:
            - mean (float): The arithmetic mean
            - median (float): The median value
            - std_dev (float): The standard deviation
            
    Raises:
        ValueError: If the input list is empty
        TypeError: If the input contains non-numeric values
        
    Examples:
        >>> calculate_statistics([1, 2, 3, 4, 5])
        {'mean': 3.0, 'median': 3.0, 'std_dev': 1.58}
    """
```

NumPy Style:
```python
def calculate_statistics(numbers):
    """
    Calculate basic statistics from a list of numbers.
    
    Parameters
    ----------
    numbers : list
        A list of numeric values
        
    Returns
    -------
    dict
        A dictionary containing:
        - mean (float): The arithmetic mean
        - median (float): The median value
        - std_dev (float): The standard deviation
        
    Raises
    ------
    ValueError
        If the input list is empty
    TypeError
        If the input contains non-numeric values
        
    Examples
    --------
    >>> calculate_statistics([1, 2, 3, 4, 5])
    {'mean': 3.0, 'median': 3.0, 'std_dev': 1.58}
    """
```

reStructuredText Style:
```python
def calculate_statistics(numbers):
    """
    Calculate basic statistics from a list of numbers.
    
    :param numbers: A list of numeric values
    :type numbers: list
    
    :return: A dictionary containing statistics
    :rtype: dict
    
    :raises ValueError: If the input list is empty
    :raises TypeError: If the input contains non-numeric values
    
    The returned dictionary contains:
    
    * mean - The arithmetic mean
    * median - The median value
    * std_dev - The standard deviation
    
    Example::
    
        >>> calculate_statistics([1, 2, 3, 4, 5])
        {'mean': 3.0, 'median': 3.0, 'std_dev': 1.58}
    """
```

### Part 2: Generating Documentation with Sphinx

Set up Sphinx documentation:

```bash
# Install Sphinx
pip install sphinx sphinx-rtd-theme

# Create a docs directory
mkdir docs
cd docs

# Initialize Sphinx
sphinx-quickstart
```

Configure `conf.py`:

```python
# Add these lines to conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

# Theme
html_theme = 'sphinx_rtd_theme'
```

Create an API documentation file (`api.rst`):

```rst
API Documentation
================

.. automodule:: my_package.core
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: my_package.helpers
   :members:
   :undoc-members:
   :show-inheritance:
```

### Part 3: Creating a GitHub Pages Website

1. Build the documentation:

```bash
cd docs
make html
```

2. Create a `gh-pages` branch and push the documentation:

```bash
git checkout --orphan gh-pages
git rm -rf .
touch .nojekyll
mkdir docs
cp -r docs/_build/html/* docs/
git add .nojekyll docs
git commit -m "Initial documentation"
git push origin gh-pages
```

### Part 4: Creating a README Badge

Add badges to your README.md:

```markdown
# My Project

[![Documentation Status](https://img.shields.io/readthedocs/myproject/latest?style=flat-square)](https://myproject.readthedocs.io/)
[![PyPI version](https://img.shields.io/pypi/v/myproject?style=flat-square)](https://pypi.org/project/myproject/)
[![Python versions](https://img.shields.io/pypi/pyversions/myproject?style=flat-square)](https://pypi.org/project/myproject/)
[![License](https://img.shields.io/github/license/yourusername/myproject?style=flat-square)](https://github.com/yourusername/myproject/blob/main/LICENSE)
```

## Questions to Answer

1. What are the key differences between the three docstring styles?
2. Why is documentation important for Python projects?
3. What are the advantages of tools like Sphinx over simple README files?
4. How can you verify that your documentation is complete and up-to-date?
5. What elements should always be included in a project's README?

## Challenge

For a Python package of your choice:
1. Add comprehensive docstrings to all public functions and classes
2. Set up Sphinx documentation with autodoc
3. Create a Read the Docs or GitHub Pages website
4. Add badges to the README
5. Create a user guide with examples
