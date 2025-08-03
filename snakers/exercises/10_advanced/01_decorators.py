"""
Exercise 10.1: Decorators

Learn about Python decorators for modifying functions.

Tasks:
1. Complete the decorator functions below
2. Apply decorators to modify function behavior
3. Learn about decorator syntax and function wrapping

Topics covered:
- Basic decorator pattern
- Function wrapping with functools.wraps
- Decorators with parameters
- Multiple decorators
"""

from typing import Callable, Any, List, Dict
import time
import functools

def timer_decorator(func: Callable) -> Callable:
    """
    Decorator that times how long a function takes to execute.
    
    Args:
        func: Function to decorate
        
    Returns:
        Wrapped function that prints timing information
    """
    # TODO: Create a wrapper function
    # TODO: Record start time before calling func
    # TODO: Record end time after calling func
    # TODO: Print execution time
    # TODO: Return the result of the function call
    pass

def debug_decorator(func: Callable) -> Callable:
    """
    Decorator that prints function arguments and return value.
    
    Args:
        func: Function to decorate
        
    Returns:
        Wrapped function that prints debug information
    """
    # TODO: Create a wrapper function
    # TODO: Print function name and arguments
    # TODO: Call the function and capture the result
    # TODO: Print the return value
    # TODO: Return the result
    pass

def repeat_decorator(times: int) -> Callable:
    """
    Decorator that repeats a function a specified number of times.
    
    Args:
        times: Number of times to repeat
        
    Returns:
        Decorator function
    """
    # TODO: Create a decorator function that takes the function to decorate
    # TODO: Create a wrapper that calls the function 'times' times
    # TODO: Return the wrapper
    pass

def memoize_decorator(func: Callable) -> Callable:
    """
    Decorator that memoizes (caches) function results.
    
    Args:
        func: Function to decorate
        
    Returns:
        Wrapped function that caches results
    """
    # TODO: Create a cache dictionary
    # TODO: Create a wrapper function
    # TODO: Check if arguments are in cache
    # TODO: If yes, return cached result
    # TODO: If no, call function, store result in cache, and return it
    pass

def validation_decorator(types: List[type]) -> Callable:
    """
    Decorator that validates function arguments against specified types.
    
    Args:
        types: List of types for positional arguments
        
    Returns:
        Decorator function
    """
    # TODO: Create a decorator function that takes the function to decorate
    # TODO: Create a wrapper that validates arguments against types
    # TODO: Raise TypeError if validation fails
    # TODO: Call and return the function if validation passes
    pass

@timer_decorator
def slow_function(n: int) -> int:
    """A deliberately slow function for testing timer decorator."""
    time.sleep(0.1)
    return n * n

@debug_decorator
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@repeat_decorator(3)
def greet(name: str) -> str:
    """Greet a person."""
    return f"Hello, {name}!"

@memoize_decorator
def fibonacci(n: int) -> int:
    """Calculate Fibonacci number (inefficient recursive version)."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@validation_decorator([int, int])
def divide(a: int, b: int) -> float:
    """Divide a by b."""
    return a / b

if __name__ == "__main__":
    # Test timer decorator
    result = slow_function(5)
    print(f"Result: {result}\n")
    
    # Test debug decorator
    add_numbers(3, 4)
    print()
    
    # Test repeat decorator
    greeting = greet("Alice")
    print(f"Final greeting: {greeting}\n")
    
    # Test memoize decorator
    start = time.time()
    fib_result = fibonacci(30)  # This would be very slow without memoization
    end = time.time()
    print(f"Fibonacci(30) = {fib_result}, calculated in {end - start:.6f} seconds\n")
    
    # Test validation decorator
    try:
        result = divide(10, 2)
        print(f"10 / 2 = {result}")
        result = divide("10", 2)  # Should raise TypeError
        print(f"'10' / 2 = {result}")
    except TypeError as e:
        print(f"TypeError: {e}")
