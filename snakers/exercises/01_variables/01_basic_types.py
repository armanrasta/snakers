"""
Exercise 1.1: Basic Variable Types

Learn about Python's fundamental data types and proper variable declaration.

Tasks:
1. Create variables with proper type hints
2. Understand mutability vs immutability
3. Practice type conversion and validation

Topics covered:
- int, float, str, bool
- Type hints and annotations
- Variable naming conventions
- Basic type operations
"""

from typing import Any

def declare_basic_variables() -> dict[str, Any]:
    """Create and return basic variables with proper types"""
    # TODO: Create an integer variable 'count' with value 42
    # TODO: Create a float variable 'price' with value 19.99
    # TODO: Create a string variable 'product_name' with value "Python Book"
    # TODO: Create a boolean variable 'is_available' with value True
    
    # TODO: Return all variables in a dictionary
    pass

def convert_types(value: str) -> tuple[int, float, bool]:
    """Convert string to different types safely"""
    # TODO: Convert string to int (handle ValueError)
    # TODO: Convert string to float (handle ValueError)
    # TODO: Convert string to bool (remember: only empty string is False)
    # TODO: Return tuple of (int_val, float_val, bool_val)
    pass

def validate_number_range(number: int, min_val: int = 0, max_val: int = 100) -> bool:
    """Check if number is within specified range"""
    # TODO: Validate that number is between min_val and max_val (inclusive)
    # TODO: Add proper type checking
    pass

if __name__ == "__main__":
    variables = declare_basic_variables()
    print("Variables:", variables)
    
    # Test type conversion
    test_values = ["42", "3.14", "hello", ""]
    for val in test_values:
        try:
            result = convert_types(val)
            print(f"'{val}' -> {result}")
        except Exception as e:
            print(f"Error converting '{val}': {e}")
