"""
Exercise 2.3: Tuples and Unpacking

Learn about Python tuples, tuple unpacking, and basic operations.

Tasks:
1. Complete the functions below
2. Learn tuple unpacking and basic operations
3. Practice with coordinate pairs and data grouping

Topics covered:
- Creating and accessing tuples
- Tuple unpacking (a, b = tuple)
- Using tuples for coordinates/pairs
- Basic tuple operations
"""

from typing import Tuple, List

def get_coordinates() -> Tuple[int, int]:
    """
    Return a tuple representing coordinates (x=10, y=20).
    
    Returns:
        Tuple of (x, y) coordinates
    
    Example:
        >>> get_coordinates()
        (10, 20)
    """
    # TODO: Return a tuple with x=10, y=20
    pass

def swap_coordinates(point: Tuple[int, int]) -> Tuple[int, int]:
    """
    Swap x and y coordinates using tuple unpacking.
    
    Args:
        point: Tuple of (x, y) coordinates
        
    Returns:
        Tuple with swapped coordinates (y, x)
    
    Example:
        >>> swap_coordinates((3, 7))
        (7, 3)
    """
    # TODO: Use tuple unpacking to get x and y
    # TODO: Return new tuple with y, x
    pass

def calculate_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """
    Calculate distance between two points.
    
    Args:
        point1: First point (x1, y1)
        point2: Second point (x2, y2)
        
    Returns:
        Distance between points
    
    Example:
        >>> calculate_distance((0, 0), (3, 4))
        5.0
    """
    # TODO: Unpack both tuples to get x1, y1, x2, y2
    # TODO: Calculate distance using: sqrt((x2-x1)**2 + (y2-y1)**2)
    # TODO: Import math module if needed
    pass

def get_name_and_age() -> Tuple[str, int]:
    """
    Return a tuple with your name and age.
    
    Returns:
        Tuple of (name, age)
    """
    # TODO: Return tuple with your name and age (use any values)
    pass

def make_pairs(numbers: List[int]) -> List[Tuple[int, int]]:
    """
    Create pairs of adjacent numbers from a list.
    
    Args:
        numbers: List of integers
        
    Returns:
        List of tuples with adjacent pairs
    
    Example:
        >>> make_pairs([1, 2, 3, 4])
        [(1, 2), (2, 3), (3, 4)]
    """
    # TODO: Create pairs of adjacent numbers
    # TODO: Hint: use range(len(numbers) - 1)
    pass

def find_max_coordinate(points: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    Find the point with the largest x + y sum.
    
    Args:
        points: List of coordinate tuples
        
    Returns:
        Point with maximum x + y sum
    
    Example:
        >>> find_max_coordinate([(1, 2), (3, 4), (2, 1)])
        (3, 4)
    """
    # TODO: Find point where x + y is maximum
    # TODO: Use max() function with a key
    pass

if __name__ == "__main__":
    # Test your functions
    print("Basic coordinates:", get_coordinates())
    
    point = (5, 10)
    swapped = swap_coordinates(point)
    print(f"Original: {point}, Swapped: {swapped}")
    
    distance = calculate_distance((0, 0), (3, 4))
    print(f"Distance: {distance}")
    
    name_age = get_name_and_age()
    print(f"Name and age: {name_age}")
    
    pairs = make_pairs([1, 2, 3, 4, 5])
    print(f"Pairs: {pairs}")
    
    points = [(1, 2), (3, 4), (2, 1), (0, 8)]
    max_point = find_max_coordinate(points)
    print(f"Max coordinate sum: {max_point}")
    
    points = [(1, 2), (3, 4), (2, 1), (0, 8)]
    max_point = find_max_coordinate(points)
    print(f"Max coordinate sum: {max_point}")
