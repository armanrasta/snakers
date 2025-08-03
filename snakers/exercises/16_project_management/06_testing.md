# Testing in Python

Learn how to create effective tests for your Python code.

## Exercise: Testing Python Code

### Part 1: Unit Testing with pytest

Install pytest:

```bash
pip install pytest pytest-cov
```

Create a simple function to test in `calculator.py`:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Create tests in `test_calculator.py`:

```python
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(1, 1) == 0
    assert subtract(1, 2) == -1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 3) == -2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
```

Run the tests:

```bash
pytest
```

### Part 2: Test Coverage

Check test coverage:

```bash
pytest --cov=calculator
```

Generate a coverage report:

```bash
pytest --cov=calculator --cov-report=html
```

### Part 3: Test Fixtures

Create a test with fixtures:

```python
import pytest
from calculator import add, subtract, multiply, divide

@pytest.fixture
def sample_numbers():
    return (10, 5)

def test_add_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 15

def test_subtract_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 5

def test_multiply_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert multiply(a, b) == 50

def test_divide_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert divide(a, b) == 2
```

### Part 4: Parameterized Tests

Create parameterized tests:

```python
import pytest
from calculator import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (-1, -1, -2),
])
def test_add_parameterized(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 1, 1),
    (1, 1, 0),
    (1, 2, -1),
])
def test_subtract_parameterized(a, b, expected):
    assert subtract(a, b) == expected
```

### Part 5: Setting Up Continuous Integration

Create a GitHub Actions workflow file in `.github/workflows/tests.yml`:

```yaml
name: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        pip install pytest pytest-cov
    - name: Test with pytest
      run: |
        pytest --cov=./ --cov-report=xml
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v1
```

## Questions to Answer

1. What is the difference between unit tests, integration tests, and functional tests?
2. Why is test coverage important? Is 100% coverage always necessary?
3. What are test fixtures and when should you use them?
4. How do parameterized tests improve your test suite?
5. What are the benefits of continuous integration for testing?

## Challenge

For an existing Python package:
1. Achieve at least 90% test coverage
2. Include unit tests, integration tests, and edge cases
3. Use fixtures and parameterized tests
4. Set up a continuous integration pipeline
5. Add a code coverage badge to the README
