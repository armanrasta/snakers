"""
Exercise 2.3: Advanced Tuple Operations

Learn about Python tuples, tuple unpacking, and functional programming patterns.

Tasks:
1. Complete the functions below with proper error handling
2. Use tuple unpacking and functional programming patterns
3. Handle all edge cases properly
4. Implement performance-conscious solutions

Topics covered:
- Tuple unpacking
- Functional programming with filter/map/reduce
- Performance considerations
- Memory efficiency
- Type safety with generics
"""


from typing import Tuple, List, TypeVar, Callable, Iterator

T = TypeVar('T')
def filter_positive_tuples(data: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Filter tuples containing only positive integers.
    
    Args:
        data: List of tuples with two integers each
        
    Returns:
        List of tuples where both integers are positive
        
    Raises:
        TypeError: If input is not a list or contains non-tuple elements
        ValueError: If tuples do not contain exactly two integers
    
    Examples:
        >>> filter_positive_tuples([(1, 2), (-1, 3), (4, 5)])
        [(1, 2), (4, 5)]
        >>> filter_positive_tuples([])
        []
    """

    if not isinstance(data, list):
        raise TypeError("Input must be a list")

    result = []
    for item in data:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Each item must be a tuple of two integers")
        a, b = item
        if a > 0 and b > 0:
            result.append(item)
    return result
