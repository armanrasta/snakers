"""
Exercise 2.1: List Operations

Learn about Python lists, list comprehensions, and basic operations.

Tasks:
1. Complete the functions below
2. Use list comprehensions where helpful
3. Practice with common list operations

Topics covered:
- List creation and access
- List comprehensions
- Common list methods (append, extend, etc.)
- Basic filtering and mapping
"""

from typing import List

def create_number_list() -> List[int]:
    """
    Create and return a list of numbers from 1 to 10.
    
    Returns:
        List of integers [1, 2, 3, ..., 10]
    """
    # TODO: Create a list with numbers 1 to 10
    # TODO: You can use range() and list()
    pass

def filter_even_numbers(numbers: List[int]) -> List[int]:
    """
    Return a list containing only even numbers.
    
    Args:
        numbers: List of integers to filter
        
    Returns:
        List of even integers
        
    Example:
        >>> filter_even_numbers([1, 2, 3, 4, 5])
        [2, 4]
    """
    # TODO: Use list comprehension to filter even numbers (x % 2 == 0)
    pass

def double_numbers(numbers: List[int]) -> List[int]:
    """
    Return a list with all numbers doubled.
    
    Args:
        numbers: List of integers
        
    Returns:
        List with each number multiplied by 2
        
    Example:
        >>> double_numbers([1, 2, 3])
        [2, 4, 6]
    """
    # TODO: Use list comprehension to double each number
    pass

def find_longest_word(words: List[str]) -> str:
    """
    Find the longest word in a list.
    
    Args:
        words: List of words
        
    Returns:
        The longest word
        
    Example:
        >>> find_longest_word(["cat", "elephant", "dog"])
        "elephant"
    """
    # TODO: Use max() with key parameter
    # TODO: key should be len (length function)
    pass

def count_vowels_in_words(words: List[str]) -> List[int]:
    """
    Count vowels in each word.
    
    Args:
        words: List of words
        
    Returns:
        List of vowel counts for each word
        
    Example:
        >>> count_vowels_in_words(["hello", "world"])
        [2, 1]
    """
    # TODO: For each word, count vowels (a, e, i, o, u)
    # TODO: Use list comprehension
    pass

def combine_lists(list1: List[int], list2: List[int]) -> List[int]:
    """
    Combine two lists and remove duplicates.
    
    Args:
        list1: First list
        list2: Second list
        
    Returns:
        Combined list without duplicates
        
    Example:
        >>> combine_lists([1, 2, 3], [3, 4, 5])
        [1, 2, 3, 4, 5]
    """
    # TODO: Combine lists and convert to set to remove duplicates
    # TODO: Convert back to list and sort
    pass

if __name__ == "__main__":
    # Test your functions
    numbers = create_number_list()
    print("Numbers 1-10:", numbers)
    
    evens = filter_even_numbers(numbers)
    print("Even numbers:", evens)
    
    doubled = double_numbers([1, 2, 3, 4])
    print("Doubled:", doubled)
    
    longest = find_longest_word(["cat", "elephant", "dog", "butterfly"])
    print("Longest word:", longest)
    
    vowel_counts = count_vowels_in_words(["hello", "world", "python"])
    print("Vowel counts:", vowel_counts)
    
    combined = combine_lists([1, 2, 3], [3, 4, 5, 6])
    print("Combined unique:", combined)
    pass

if __name__ == "__main__":
    # Test your functions
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_strings = ["hello", "world", "python", "programming", ""]
    
    print("Even numbers:", filter_even_numbers(test_numbers))
    print("Sum of squares:", sum_of_squares(test_numbers))
    print("Reversed strings:", reverse_strings(test_strings))
    print("Longest string:", find_longest_string(test_strings))
    
    # Test chunking
    chunks = chunk_list(test_numbers, 3)
    print("Chunks:", chunks)
    
    # Test flattening
    nested = [[1, 2], [3, 4], [5, 6]]
    flattened = flatten_nested_list(nested)
    print("Flattened:", flattened)
