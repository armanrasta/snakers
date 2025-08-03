"""
Exercise 2.4: Sets

Learn about Python sets, set operations, and applications.

Tasks:
1. Complete the functions below
2. Practice with set creation and operations
3. Learn about common set use cases

Topics covered:
- Set creation and properties
- Set operations (union, intersection, difference)
- Removing duplicates with sets
- Membership testing
"""

from typing import Set, List, Any

def create_unique_numbers() -> Set[int]:
    """
    Create a set of unique numbers.
    
    Returns:
        Set containing numbers 1, 2, 3, 4, 5
        
    Example:
        >>> create_unique_numbers()
        {1, 2, 3, 4, 5}
    """
    # TODO: Create a set with numbers 1 through 5
    pass

def remove_duplicates(items: List[Any]) -> List[Any]:
    """
    Remove duplicates from a list while preserving order.
    
    Args:
        items: List possibly containing duplicates
        
    Returns:
        List with duplicates removed, original order preserved
        
    Example:
        >>> remove_duplicates([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
    """
    # TODO: Use a set to remove duplicates
    # TODO: Preserve the original order of items
    pass

def find_common_elements(list1: List[int], list2: List[int]) -> Set[int]:
    """
    Find common elements between two lists.
    
    Args:
        list1: First list
        list2: Second list
        
    Returns:
        Set of elements that appear in both lists
        
    Example:
        >>> find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
        {3, 4}
    """
    # TODO: Convert lists to sets
    # TODO: Use intersection to find common elements
    pass

def find_unique_to_first(list1: List[int], list2: List[int]) -> Set[int]:
    """
    Find elements that are in the first list but not in the second.
    
    Args:
        list1: First list
        list2: Second list
        
    Returns:
        Set of elements unique to first list
        
    Example:
        >>> find_unique_to_first([1, 2, 3, 4], [3, 4, 5, 6])
        {1, 2}
    """
    # TODO: Convert lists to sets
    # TODO: Use set difference (-)
    pass

def is_subset(set1: Set[int], set2: Set[int]) -> bool:
    """
    Check if the first set is a subset of the second.
    
    Args:
        set1: First set
        set2: Second set
        
    Returns:
        True if first set is subset of second, False otherwise
        
    Example:
        >>> is_subset({1, 2}, {1, 2, 3, 4})
        True
    """
    # TODO: Use issubset() method or <= operator
    pass

def find_all_unique_elements(list1: List[int], list2: List[int]) -> Set[int]:
    """
    Find elements that are in exactly one of the lists (not in both).
    
    Args:
        list1: First list
        list2: Second list
        
    Returns:
        Set of elements that appear in exactly one list
        
    Example:
        >>> find_all_unique_elements([1, 2, 3, 4], [3, 4, 5, 6])
        {1, 2, 5, 6}
    """
    # TODO: Use symmetric difference (^)
    pass

if __name__ == "__main__":
    # Test your functions
    unique_nums = create_unique_numbers()
    print("Unique numbers:", unique_nums)
    
    duplicate_list = [1, 2, 2, 3, 4, 4, 1, 5]
    no_duplicates = remove_duplicates(duplicate_list)
    print(f"Original: {duplicate_list}, No duplicates: {no_duplicates}")
    
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    
    common = find_common_elements(list_a, list_b)
    print(f"Common elements: {common}")
    
    unique_to_a = find_unique_to_first(list_a, list_b)
    print(f"Unique to first list: {unique_to_a}")
    
    set_x = {1, 2}
    set_y = {1, 2, 3, 4}
    print(f"Is {set_x} a subset of {set_y}? {is_subset(set_x, set_y)}")
    
    symmetric_diff = find_all_unique_elements(list_a, list_b)
    print(f"Elements in exactly one list: {symmetric_diff}")
