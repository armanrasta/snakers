"""
Exercise 5.1: Basic Exception Handling

Learn about Python's exception handling mechanisms.

Tasks:
1. Complete the functions below
2. Practice with try/except blocks
3. Learn about different exception types

Topics covered:
- try/except/else/finally blocks
- Common exception types
- Exception handling best practices
- Creating custom exceptions
"""

from typing import Any, List, Dict, Union

def safe_divide(a: float, b: float) -> Union[float, str]:
    """
    Safely divide two numbers, handling division by zero.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Result of division or error message
        
    Example:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(10, 0)
        "Cannot divide by zero"
    """
    # TODO: Use try/except to catch ZeroDivisionError
    pass

def parse_int(text: str) -> Union[int, None]:
    """
    Try to parse string as integer, return None if not possible.
    
    Args:
        text: String to parse
        
    Returns:
        Integer value or None if conversion fails
        
    Example:
        >>> parse_int("123")
        123
        >>> parse_int("abc")
        None
    """
    # TODO: Use try/except to catch ValueError
    pass

def get_item_safely(items: List[Any], index: int) -> Any:
    """
    Safely get item from list, handling index errors.
    
    Args:
        items: List to retrieve from
        index: Index to access
        
    Returns:
        Item at index or None if index is invalid
        
    Example:
        >>> get_item_safely([1, 2, 3], 1)
        2
        >>> get_item_safely([1, 2, 3], 10)
        None
    """
    # TODO: Use try/except to catch IndexError
    pass

def read_file_content(filename: str) -> Union[str, str]:
    """
    Read and return file content, handling file not found errors.
    
    Args:
        filename: Name of file to read
        
    Returns:
        File content or error message
        
    Example:
        >>> read_file_content("existing.txt")
        "File content..."
        >>> read_file_content("nonexistent.txt")
        "File not found"
    """
    # TODO: Use try/except to catch FileNotFoundError
    pass

def access_dict_key(data: Dict[str, Any], key: str) -> Any:
    """
    Safely access dictionary key with a useful error message.
    
    Args:
        data: Dictionary to access
        key: Key to retrieve
        
    Returns:
        Value for key or error message
        
    Example:
        >>> access_dict_key({"name": "Alice"}, "name")
        "Alice"
        >>> access_dict_key({"name": "Alice"}, "age")
        "Key 'age' not found in dictionary"
    """
    # TODO: Use try/except to catch KeyError
    pass

def convert_to_proper_type(value: str) -> Any:
    """
    Try to convert string to its proper type (int, float, or keep as string).
    
    Args:
        value: String to convert
        
    Returns:
        Converted value
        
    Example:
        >>> convert_to_proper_type("123")
        123
        >>> convert_to_proper_type("3.14")
        3.14
        >>> convert_to_proper_type("hello")
        "hello"
    """
    # TODO: Try to convert to int, then float, keep as string if both fail
    pass

def validate_age(age: Any) -> Union[int, str]:
    """
    Validate that age is a positive integer.
    
    Args:
        age: Value to validate
        
    Returns:
        Validated age or error message
        
    Example:
        >>> validate_age(25)
        25
        >>> validate_age(-5)
        "Age cannot be negative"
        >>> validate_age("25")
        "Age must be an integer"
    """
    # TODO: Use multiple exception handling to validate
    pass

if __name__ == "__main__":
    # Test your functions
    print(f"10/2 = {safe_divide(10, 2)}")
    print(f"10/0 = {safe_divide(10, 0)}")
    
    print(f"Parse '123': {parse_int('123')}")
    print(f"Parse 'abc': {parse_int('abc')}")
    
    test_list = [1, 2, 3]
    print(f"Item at index 1: {get_item_safely(test_list, 1)}")
    print(f"Item at index 10: {get_item_safely(test_list, 10)}")
    
    print(f"Read 'example.txt': {read_file_content('example.txt')}")
    
    test_dict = {"name": "Alice", "age": 30}
    print(f"Dict key 'name': {access_dict_key(test_dict, 'name')}")
    print(f"Dict key 'email': {access_dict_key(test_dict, 'email')}")
    
    print(f"Convert '123': {convert_to_proper_type('123')}")
    print(f"Convert '3.14': {convert_to_proper_type('3.14')}")
    print(f"Convert 'hello': {convert_to_proper_type('hello')}")
    
    print(f"Validate age 25: {validate_age(25)}")
    print(f"Validate age -5: {validate_age(-5)}")
    print(f"Validate age 'abc': {validate_age('abc')}")
