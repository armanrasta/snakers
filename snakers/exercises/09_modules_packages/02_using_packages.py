"""
Exercise 9.2: Working with Packages

Learn about Python packages and how to use them.

Tasks:
1. Complete the functions below
2. Import and use functions from the my_package package
3. Learn about package structure and imports

Topics covered:
- Package structure
- Absolute and relative imports
- Creating your own packages
- Importing from packages
"""

from typing import List, Dict, Any, Callable
import sys
import os

def add_package_to_path() -> None:
    """
    Add the current directory to Python's module search path.
    """
    # TODO: Use sys.path.append to add the current directory
    pass

def import_from_my_package() -> Dict[str, Callable]:
    """
    Import functions from my_package and return them in a dictionary.
    
    Returns:
        Dictionary mapping function names to function objects
    """
    # TODO: Import add, subtract from my_package.utils
    # TODO: Import square, cube from my_package.math_functions
    # TODO: Return a dictionary with function names as keys and functions as values
    pass

def calculate_with_package(a: int, b: int) -> Dict[str, int]:
    """
    Perform calculations using functions from my_package.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Dictionary with results of different operations
    """
    # TODO: Import functions from my_package
    # TODO: Calculate add, subtract, square of a, cube of b
    # TODO: Return dictionary with all results
    pass

def list_package_contents(package_name: str) -> Dict[str, List[str]]:
    """
    List the modules and functions in a package.
    
    Args:
        package_name: Name of the package
        
    Returns:
        Dictionary with modules and their functions
    """
    # TODO: Import the package dynamically
    # TODO: Get all non-private modules (no underscore prefix)
    # TODO: For each module, get all non-private functions
    # TODO: Return a dictionary mapping module names to function lists
    pass

def execute_package_function(function_name: str, *args: Any) -> Any:
    """
    Execute a function from my_package by name.
    
    Args:
        function_name: Name of the function to execute
        *args: Arguments to pass to the function
        
    Returns:
        Result of the function call
    """
    # TODO: Import my_package
    # TODO: Get the named function (may be in a submodule)
    # TODO: Execute the function with the provided arguments
    # TODO: Return the result
    pass

if __name__ == "__main__":
    # Make sure the package is accessible
    add_package_to_path()
    
    # Test importing from package
    functions = import_from_my_package()
    print("Imported functions:")
    for name, func in functions.items():
        print(f"  {name}: {func}")
    
    # Test calculations
    results = calculate_with_package(5, 3)
    print("Calculation results:")
    for operation, result in results.items():
        print(f"  {operation}: {result}")
    
    # List package contents
    try:
        package_contents = list_package_contents("my_package")
        print("Package contents:")
        for module, funcs in package_contents.items():
            print(f"  {module}: {funcs}")
    except ImportError as e:
        print(f"Error importing package: {e}")
    
    # Test function execution
    add_result = execute_package_function("add", 10, 20)
    print(f"add(10, 20) = {add_result}")
    
    square_result = execute_package_function("square", 7)
    print(f"square(7) = {square_result}")
