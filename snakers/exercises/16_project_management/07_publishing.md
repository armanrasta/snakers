# Publishing Python Packages

Learn how to prepare and publish a Python package to PyPI.

## Exercise: Publishing a Package to PyPI

### Part 1: Setting Up Your Package

Create a package-ready project structure:

```
my_package/
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── core.py
├── tests/
│   └── test_core.py
├── pyproject.toml
├── LICENSE
└── README.md
```

Create a modern `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-awesome-package"
version = "0.1.0"
description = "A sample Python package"
readme = "README.md"
authors = [{name = "Your Name", email = "your.email@example.com"}]
license = {text = "MIT"}
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]
keywords = ["sample", "package", "example"]
dependencies = [
    "requests>=2.25.0",
]
requires-python = ">=3.7"

[project.urls]
Homepage = "https://github.com/yourusername/my-awesome-package"
Documentation = "https://my-awesome-package.readthedocs.io/"
Repository = "https://github.com/yourusername/my-awesome-package.git"
Issues = "https://github.com/yourusername/my-awesome-package/issues"

[project.scripts]
my-command = "my_package.cli:main"

[tool.setuptools]
package-dir = {"" = "src"}
packages = ["my_package"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
```

### Part 2: Building Your Package

Install build tools:

```bash
pip install build twine
```

Build your package:

```bash
python -m build
```

This creates two files in the `dist/` directory:
- A source distribution (`.tar.gz`)
- A wheel distribution (`.whl`)

### Part 3: Testing Your Package Locally

Create a test virtual environment:

```bash
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate
```

Install your package from the local build:

```bash
pip install dist/my_awesome_package-0.1.0-py3-none-any.whl
```

Try importing and using your package:

```python
from my_package import core
# Use your package
```

### Part 4: Uploading to TestPyPI

Register an account on TestPyPI: https://test.pypi.org/account/register/

Upload your package to TestPyPI:

```bash
python -m twine upload --repository testpypi dist/*
```

Install your package from TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ my-awesome-package
```

### Part 5: Publishing to PyPI

Register an account on PyPI: https://pypi.org/account/register/

Upload your package to PyPI:

```bash
python -m twine upload dist/*
```

Now anyone can install your package:

```bash
pip install my-awesome-package
```

### Part 6: Automating Releases with GitHub Actions

Create a workflow file in `.github/workflows/publish.yml`:

```yaml
name: Publish Python Package

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build and publish
      env:
        TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
        TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}
      run: |
        python -m build
        twine upload dist/*
```

## Questions to Answer

1. What's the difference between a source distribution and a wheel distribution?
2. Why should you test your package on TestPyPI before publishing to PyPI?
3. What is the purpose of classifiers in your package metadata?
4. How do you manage version numbers for your package?
5. What are the advantages of using GitHub Actions for automating releases?

## Challenge

Create and publish a simple utility package that:
1. Solves a specific problem or provides useful functionality
2. Has comprehensive documentation
3. Includes proper tests
4. Uses semantic versioning
5. Is published to PyPI with automated releases
