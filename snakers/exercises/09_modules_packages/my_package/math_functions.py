"""
Math functions for my_package.
"""

def square(x: int) -> int:
    """Square a number."""
    return x * x

def cube(x: int) -> int:
    """Cube a number."""
    return x * x * x

def factorial(n: int) -> int:
    """Calculate n factorial."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)
