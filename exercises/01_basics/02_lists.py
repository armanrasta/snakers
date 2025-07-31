"""
Exercise 2: Lists and Loops

Learn about Python lists, list comprehensions, and iteration.

Tasks:
1. Complete the functions below
2. Use list comprehensions where appropriate
3. Handle edge cases properly
"""

from typing import List

def filter_even_numbers(numbers: List[int]) -> list[int]:
    """Return a list containing only even numbers"""
    # TODO: Use list comprehension to filter even numbers
    pass

def sum_of_squares(numbers: List[int]) -> int:
    """Return the sum of squares of all numbers"""
    # TODO: Calculate sum of squares (hint: use sum() and list comprehension)
    pass

def reverse_strings(strings: List[str]) -> List[str]:
    """Return a list with all strings reversed"""
    # TODO: Reverse each string in the list
    pass

def find_longest_string(strings: List[str]) -> str:
    """Find and return the longest string"""
    # TODO: Handle empty list case
    # TODO: Return the longest string (use max() with key parameter)
    pass

if __name__ == "__main__":
    # Test your functions
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_strings = ["hello", "world", "python", "programming"]
    
    print("Even numbers:", filter_even_numbers(test_numbers))
    print("Sum of squares:", sum_of_squares(test_numbers))
    print("Reversed strings:", reverse_strings(test_strings))
    print("Longest string:", find_longest_string(test_strings))
