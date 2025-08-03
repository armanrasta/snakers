"""
Exercise 7.1: Functional Programming Basics

Learn about Python's functional programming capabilities.

Tasks:
1. Complete the functions below
2. Use map(), filter(), and reduce()
3. Practice with lambda functions and list comprehensions

Topics covered:
- Pure functions
- Lambda expressions
- Higher-order functions
- Map, filter, and reduce operations
"""

from typing import List, Callable, TypeVar, Any
from functools import reduce

T = TypeVar('T')
R = TypeVar('R')

def double_numbers(numbers: List[int]) -> List[int]:
    """
    Double all numbers using map and lambda.
    
    Args:
        numbers: List of integers
        
    Returns:
        List with all numbers doubled
        
    Example:
        >>> double_numbers([1, 2, 3])
        [2, 4, 6]
    """
    # TODO: Use map() and lambda to double each number
    # TODO: Convert map object to list
    pass

def filter_positive_numbers(numbers: List[int]) -> List[int]:
    """
    Filter only positive numbers using filter and lambda.
    
    Args:
        numbers: List of integers
        
    Returns:
        List with only positive numbers
        
    Example:
        >>> filter_positive_numbers([-1, 0, 2, -3, 5])
        [2, 5]
    """
    # TODO: Use filter() and lambda to keep only positive numbers
    # TODO: Convert filter object to list
    pass

def sum_of_squares(numbers: List[int]) -> int:
    """
    Calculate sum of squares using reduce and lambda.
    
    Args:
        numbers: List of integers
        
    Returns:
        Sum of squares of all numbers
        
    Example:
        >>> sum_of_squares([1, 2, 3])
        14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
    """
    # TODO: Use reduce() and lambda to sum the squares
    # TODO: Define the lambda to add the square of y to the accumulator x
    pass

def apply_function_to_each(func: Callable[[int], int], numbers: List[int]) -> List[int]:
    """
    Apply a function to each number in the list.
    
    Args:
        func: Function that takes an integer and returns an integer
        numbers: List of integers
        
    Returns:
        List with function applied to each number
        
    Example:
        >>> apply_function_to_each(lambda x: x * x, [1, 2, 3])
        [1, 4, 9]
    """
    # TODO: Use map to apply the function to each number
    pass

def sort_by_length(strings: List[str]) -> List[str]:
    """
    Sort strings by their length.
    
    Args:
        strings: List of strings
        
    Returns:
        List of strings sorted by length (shortest first)
        
    Example:
        >>> sort_by_length(["apple", "banana", "cherry", "date"])
        ["date", "apple", "cherry", "banana"]
    """
    # TODO: Use sorted() with a key function
    # TODO: The key should be the length of each string
    pass

def compose_functions(f: Callable[[T], Any], g: Callable[[Any], R]) -> Callable[[T], R]:
    """
    Compose two functions: h(x) = g(f(x))
    
    Args:
        f: First function to apply
        g: Second function to apply
        
    Returns:
        Composed function
        
    Example:
        >>> add_one = lambda x: x + 1
        >>> square = lambda x: x * x
        >>> composed = compose_functions(add_one, square)
        >>> composed(5)
        36  # square(add_one(5)) = square(6) = 36
    """
    # TODO: Return a lambda that applies f then g
    pass

if __name__ == "__main__":
    # Test your functions
    numbers = [1, 2, 3, 4, 5]
    print(f"Original numbers: {numbers}")
    print(f"Doubled: {double_numbers(numbers)}")
    
    mixed_numbers = [-2, -1, 0, 1, 2]
    print(f"Positive only: {filter_positive_numbers(mixed_numbers)}")
    
    print(f"Sum of squares for {numbers}: {sum_of_squares(numbers)}")
    
    cube = lambda x: x ** 3
    print(f"Cubed: {apply_function_to_each(cube, numbers)}")
    
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"Sorted by length: {sort_by_length(fruits)}")
    
    add_one = lambda x: x + 1
    square = lambda x: x * x
    composed = compose_functions(add_one, square)
    print(f"Composed function on 5: {composed(5)}")
