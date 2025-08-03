"""
Utility functions for my_package.
"""

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b

def _internal_function() -> str:
    """
    This is an internal function not meant to be imported.
    
    The leading underscore indicates it's for internal use only.
    """
    return "This is an internal function"
