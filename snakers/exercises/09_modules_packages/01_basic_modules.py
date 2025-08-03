"""
Exercise 9.1: Working with Modules

Learn about Python modules and imports.

Tasks:
1. Complete the functions below
2. Create and import your own modules
3. Practice with different import styles

Topics covered:
- Module creation and usage
- Import statements
- Module search path
- Standard library modules
"""

import os
import sys
import math
import random
from datetime import datetime
from typing import List, Dict, Any

def get_current_working_directory() -> str:
    """
    Get the current working directory.
    
    Returns:
        Current working directory path
    """
    # TODO: Use os module to get current working directory
    pass

def list_directory_contents(path: str = ".") -> List[str]:
    """
    List contents of a directory.
    
    Args:
        path: Directory path (default: current directory)
        
    Returns:
        List of files and directories
    """
    # TODO: Use os module to list directory contents
    pass

def get_system_info() -> Dict[str, Any]:
    """
    Get basic system information.
    
    Returns:
        Dictionary with system information
    """
    # TODO: Use sys module to get system information
    # TODO: Include platform, version, path, etc.
    pass

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.
    
    Args:
        radius: Circle radius
        
    Returns:
        Circle area
    """
    # TODO: Use math module to calculate and return circle area
    pass

def generate_random_numbers(count: int, min_val: int = 1, max_val: int = 100) -> List[int]:
    """
    Generate random numbers in a range.
    
    Args:
        count: How many numbers to generate
        min_val: Minimum value (inclusive)
        max_val: Maximum value (inclusive)
        
    Returns:
        List of random integers
    """
    # TODO: Use random module to generate random numbers
    pass

def get_current_time_formatted() -> str:
    """
    Get current time in a formatted string.
    
    Returns:
        Formatted date and time
    """
    # TODO: Use datetime module to get and format current time
    # TODO: Format as YYYY-MM-DD HH:MM:SS
    pass

def import_custom_module() -> str:
    """
    Import a custom module and return its info.
    
    Returns:
        Information from the custom module
    """
    # TODO: Import the custom module 'my_module.py' that you'll create
    # TODO: Return a string with module info
    # Note: For this to work, create my_module.py with a get_info() function
    pass

if __name__ == "__main__":
    # Test your functions
    print(f"Current directory: {get_current_working_directory()}")
    print(f"Directory contents: {list_directory_contents()}")
    
    sys_info = get_system_info()
    print("System information:")
    for key, value in sys_info.items():
        print(f"  {key}: {value}")
    
    print(f"Circle area (radius=5): {calculate_circle_area(5)}")
    
    random_nums = generate_random_numbers(5, 1, 10)
    print(f"Random numbers: {random_nums}")
    
    print(f"Current time: {get_current_time_formatted()}")
    
    # Create custom module file for testing
    with open("my_module.py", "w") as f:
        f.write('''
def get_info():
    return "This is my custom module!"
''')
    
    try:
        print(f"Custom module info: {import_custom_module()}")
    except ImportError as e:
        print(f"Error importing custom module: {e}")
