"""
Exercise 4.2: Loops

Learn about Python's loop structures and iteration techniques.

Tasks:
1. Complete the functions below
2. Practice with for and while loops
3. Learn about loop control statements and techniques

Topics covered:
- for loops with range(), lists, dictionaries
- while loops with conditions
- break, continue, and else clauses
- Nested loops
"""

from typing import List, Dict

def print_numbers_up_to(n: int) -> List[int]:
    """
    Print and return numbers from 1 up to n.
    
    Args:
        n: Upper limit
        
    Returns:
        List of numbers from 1 to n
        
    Example:
        >>> print_numbers_up_to(5)
        [1, 2, 3, 4, 5]
    """
    # TODO: Use a for loop with range()
    # TODO: Print each number and collect in a list
    pass

def sum_of_numbers(n: int) -> int:
    """
    Calculate the sum of numbers from 1 to n.
    
    Args:
        n: Upper limit
        
    Returns:
        Sum of numbers from 1 to n
        
    Example:
        >>> sum_of_numbers(5)
        15  # (1 + 2 + 3 + 4 + 5)
    """
    # TODO: Use a loop to sum numbers
    pass

def count_down(start: int) -> List[int]:
    """
    Count down from start to 1 and return the sequence.
    
    Args:
        start: Starting number
        
    Returns:
        List of numbers from start to 1
        
    Example:
        >>> count_down(5)
        [5, 4, 3, 2, 1]
    """
    # TODO: Use a while loop to count down
    pass

def find_first_odd_number(numbers: List[int]) -> int:
    """
    Find the first odd number in a list.
    
    Args:
        numbers: List of integers
        
    Returns:
        First odd number or -1 if none found
        
    Example:
        >>> find_first_odd_number([2, 4, 6, 7, 8])
        7
    """
    # TODO: Loop through numbers and use if to check for odd
    # TODO: Use break when found
    # TODO: Return -1 if no odd number is found
    pass

def double_values(numbers: List[int]) -> List[int]:
    """
    Double each value in a list using a for loop.
    
    Args:
        numbers: List of integers
        
    Returns:
        List with each value doubled
        
    Example:
        >>> double_values([1, 2, 3])
        [2, 4, 6]
    """
    # TODO: Use a for loop to double each value
    pass

def create_multiplication_table(size: int) -> List[List[int]]:
    """
    Create a multiplication table of the given size.
    
    Args:
        size: Size of the table
        
    Returns:
        Nested list representing the multiplication table
        
    Example:
        >>> create_multiplication_table(3)
        [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    """
    # TODO: Use nested loops to create the table
    pass

def count_characters(text: str) -> Dict[str, int]:
    """
    Count the occurrences of each character in text.
    
    Args:
        text: Input string
        
    Returns:
        Dictionary mapping characters to their counts
        
    Example:
        >>> count_characters("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    # TODO: Loop through text and count each character
    pass

if __name__ == "__main__":
    # Test your functions
    print("Numbers up to 5:", print_numbers_up_to(5))
    print("Sum of numbers up to 5:", sum_of_numbers(5))
    print("Countdown from 5:", count_down(5))
    
    test_numbers = [2, 4, 6, 7, 8]
    print(f"First odd in {test_numbers}:", find_first_odd_number(test_numbers))
    print("Doubled values:", double_values([1, 2, 3, 4]))
    
    multiplication_table = create_multiplication_table(3)
    print("Multiplication table 3x3:")
    for row in multiplication_table:
        print(row)
    
    char_count = count_characters("hello world")
    print("Character count:", char_count)
