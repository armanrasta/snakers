# Package Management in Python

Learn how to effectively manage Python packages using pip, poetry, and other tools.

## Exercise: Working with Pip and Package Management

### Part 1: Basic Pip Commands

Try these essential pip commands:

```bash
# Update pip itself
pip install --upgrade pip

# Install a specific version of a package
pip install requests==2.25.1

# Install the latest version
pip install requests

# Uninstall a package
pip install requests
pip uninstall -y requests

# Show information about a package
pip show requests
```

### Part 2: Using pip with Constraints

```bash
# Install with version constraints
pip install "requests>=2.24.0,<2.25.0"

# Install with extras
pip install "requests[security]"
```

### Part 3: Finding Packages

```bash
# Search for packages
pip search "http client"  # Note: This may not work due to PyPI API limitations

# Use PyPI website instead: https://pypi.org/search/?q=http+client
```

### Part 4: Using Poetry for Dependency Management

Poetry provides more advanced dependency management. Try it out:

```bash
# Install Poetry
pip install poetry

# Start a new project
poetry new myproject
cd myproject

# Add dependencies
poetry add requests
poetry add pytest --dev

# Install dependencies
poetry install

# Update dependencies
poetry update

# Export requirements.txt
poetry export -f requirements.txt -o requirements.txt
```

### Part 5: Pipenv - Another Alternative

```bash
# Install pipenv
pip install pipenv

# Create a new project
mkdir pipenv-demo
cd pipenv-demo

# Install packages with pipenv
pipenv install requests
pipenv install pytest --dev

# Activate the virtual environment
pipenv shell

# Generate a requirements file
pipenv lock -r > requirements.txt
```

## Questions to Answer

1. What are the advantages of Poetry or Pipenv over plain pip?
2. Why is specifying version constraints important in production applications?
3. What is the difference between development dependencies and regular dependencies?
4. What is a "lock file" and why is it important?
5. How would you handle a situation where two packages have conflicting dependencies?

## Challenge

Create a comparison document that outlines the pros and cons of:
1. pip + venv
2. Poetry
3. Pipenv
4. conda

Include examples of when you might choose each approach for different types of projects.
