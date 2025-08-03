"""
Exercise 7.2: Advanced Functional Programming

Learn about more advanced functional programming concepts.

Tasks:
1. Complete the functions below
2. Use closures and partial functions
3. Practice with recursion and function composition

Topics covered:
- Closures
- Partial functions
- Recursion
- Function composition chains
- Immutability
"""

from typing import List, Callable, Dict, Any, TypeVar
from functools import partial, reduce

T = TypeVar('T')
R = TypeVar('R')

def create_multiplier(factor: int) -> Callable[[int], int]:
    """
    Create a function that multiplies its argument by a specified factor.
    
    Args:
        factor: Multiplication factor
        
    Returns:
        Function that multiplies by factor
        
    Example:
        >>> double = create_multiplier(2)
        >>> double(5)
        10
    """
    # TODO: Return a lambda that multiplies its argument by factor
    pass

def curry_add(x: int) -> Callable[[int], int]:
    """
    Curry the addition function.
    
    Args:
        x: First number
        
    Returns:
        Function that adds x to its argument
        
    Example:
        >>> add_five = curry_add(5)
        >>> add_five(3)
        8
    """
    # TODO: Return a lambda that adds x to its argument
    pass

def factorial(n: int) -> int:
    """
    Calculate factorial recursively.
    
    Args:
        n: Number to calculate factorial for
        
    Returns:
        n! (n factorial)
        
    Example:
        >>> factorial(5)
        120  # 5 * 4 * 3 * 2 * 1
    """
    # TODO: Implement recursive factorial
    # TODO: Base case: n <= 1 return 1
    # TODO: Recursive case: n * factorial(n-1)
    pass

def memoize(func: Callable) -> Callable:
    """
    Create a memoized version of a function.
    
    Args:
        func: Function to memoize
        
    Returns:
        Memoized function that caches results
        
    Example:
        >>> @memoize
        ... def fib(n):
        ...     if n <= 1: return n
        ...     return fib(n-1) + fib(n-2)
    """
    cache: Dict[Any, Any] = {}
    
    # TODO: Define a wrapper function that checks cache before computing
    # TODO: Return the wrapper function
    pass

def compose(*functions: Callable) -> Callable:
    """
    Compose multiple functions: compose(f, g, h)(x) = f(g(h(x)))
    
    Args:
        *functions: Functions to compose (applied right to left)
        
    Returns:
        Composed function
        
    Example:
        >>> add_one = lambda x: x + 1
        >>> square = lambda x: x * x
        >>> composed = compose(square, add_one)
        >>> composed(5)
        36  # square(add_one(5)) = square(6) = 36
    """
    # TODO: Use reduce to compose functions
    # TODO: Use a lambda that applies g, then f to the result
    pass

def pipeline(value: Any, *functions: Callable) -> Any:
    """
    Apply a pipeline of functions to a value.
    
    Args:
        value: Initial value
        *functions: Functions to apply in sequence
        
    Returns:
        Result after applying all functions
        
    Example:
        >>> pipeline(5, lambda x: x + 1, lambda x: x * 2)
        12  # (5 + 1) * 2
    """
    # TODO: Use reduce to apply functions to value
    # TODO: The lambda should apply each function to the accumulated result
    pass

if __name__ == "__main__":
    # Test your functions
    triple = create_multiplier(3)
    print(f"Triple 7: {triple(7)}")
    
    add_ten = curry_add(10)
    print(f"10 + 5 = {add_ten(5)}")
    
    print(f"Factorial of 5: {factorial(5)}")
    
    # Test memoization
    @memoize
    def fibonacci(n: int) -> int:
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print(f"Fibonacci of 10: {fibonacci(10)}")
    print(f"Fibonacci of 20: {fibonacci(20)}")  # This would be very slow without memoization
    
    # Test composition
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    square = lambda x: x ** 2
    
    composed = compose(square, double, add_one)
    print(f"square(double(add_one(5))): {composed(5)}")  # square(double(add_one(5))) = square(double(6)) = square(12) = 144
    
    # Test pipeline
    result = pipeline(5, add_one, double, square)
    print(f"Pipeline result: {result}")  # ((5 + 1) * 2) ^ 2 = (6 * 2) ^ 2 = 12 ^ 2 = 144
