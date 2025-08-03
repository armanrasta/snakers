"""
Exercise 11.1: Unit Testing with unittest

Learn about Python's built-in unit testing framework.

Tasks:
1. Complete the functions in the Calculator class
2. Implement unit tests for each function
3. Run the tests and ensure they all pass

Topics covered:
- unittest framework
- Test cases and assertions
- Test fixtures (setUp, tearDown)
- Test discovery and execution
"""

import unittest
from typing import Union, List

class Calculator:
    """A simple calculator class with basic operations."""
    
    def __init__(self):
        self.history: List[str] = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        # TODO: Implement addition and record operation in history
        pass
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        # TODO: Implement subtraction and record operation in history
        pass
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        # TODO: Implement multiplication and record operation in history
        pass
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide a by b."""
        # TODO: Implement division with zero check and record operation in history
        pass
    
    def clear_history(self) -> None:
        """Clear the calculation history."""
        # TODO: Clear the history list
        pass
    
    def get_history(self) -> List[str]:
        """Get the calculation history."""
        # TODO: Return copy of history list
        pass


class CalculatorTests(unittest.TestCase):
    """Unit tests for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # TODO: Create a calculator instance for testing
        pass
    
    def test_add(self):
        """Test the add method."""
        # TODO: Test addition with positive numbers
        # TODO: Test addition with negative numbers
        # TODO: Test addition with floating point numbers
        pass
    
    def test_subtract(self):
        """Test the subtract method."""
        # TODO: Test subtraction with various number combinations
        pass
    
    def test_multiply(self):
        """Test the multiply method."""
        # TODO: Test multiplication with various number combinations
        pass
    
    def test_divide(self):
        """Test the divide method."""
        # TODO: Test division with various number combinations
        # TODO: Test division by zero raises ValueError
        pass
    
    def test_history(self):
        """Test the history functionality."""
        # TODO: Test that operations are properly recorded in history
        # TODO: Test that clear_history works correctly
        pass
    
    def tearDown(self):
        """Clean up after each test method."""
        # TODO: Clean up any resources if needed
        pass


if __name__ == "__main__":
    # Run the tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
