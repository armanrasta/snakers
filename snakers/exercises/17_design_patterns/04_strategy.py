"""
Exercise 17.4: The Strategy Pattern

Learn about the Strategy design pattern and its implementation in Python.

Tasks:
1. Complete the strategy implementations below
2. Understand different ways to implement strategies
3. Apply strategy pattern to make behavior configurable at runtime

Topics covered:
- Strategy pattern
- Composition over inheritance
- Runtime behavior selection
- Function-based vs class-based strategies
"""

from abc import ABC, abstractmethod
from typing import List, Callable, Dict, Any

# Method 1: Classic Strategy Pattern with Classes
class SortStrategy(ABC):
    """Abstract base class for sorting strategies."""
    
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort the data using the strategy.
        
        Args:
            data: Data to sort
            
        Returns:
            Sorted data
        """
        pass

class BubbleSort(SortStrategy):
    """Bubble sort implementation."""
    
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort using bubble sort algorithm.
        
        Args:
            data: Data to sort
            
        Returns:
            Sorted data
        """
        # TODO: Implement bubble sort
        # TODO: Return sorted list
        pass

class QuickSort(SortStrategy):
    """Quick sort implementation."""
    
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort using quick sort algorithm.
        
        Args:
            data: Data to sort
            
        Returns:
            Sorted data
        """
        # TODO: Implement quick sort (or use a helper function)
        # TODO: Return sorted list
        pass

class MergeSort(SortStrategy):
    """Merge sort implementation."""
    
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort using merge sort algorithm.
        
        Args:
            data: Data to sort
            
        Returns:
            Sorted data
        """
        # TODO: Implement merge sort (or use a helper function)
        # TODO: Return sorted list
        pass

class Sorter:
    """Context class that uses a sort strategy."""
    
    def __init__(self, strategy: SortStrategy = None):
        self.strategy = strategy or BubbleSort()
    
    def set_strategy(self, strategy: SortStrategy) -> None:
        """
        Change the sorting strategy.
        
        Args:
            strategy: New sorting strategy
        """
        # TODO: Set the strategy
        pass
    
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort data using the current strategy.
        
        Args:
            data: Data to sort
            
        Returns:
            Sorted data
        """
        # TODO: Use the strategy to sort data
        # TODO: Return the sorted data
        pass

# Method 2: Strategy Pattern with Functions
class FunctionalSorter:
    """Context class that uses function-based strategies."""
    
    def __init__(self, strategy: Callable[[List[int]], List[int]] = None):
        # TODO: Set default strategy to Python's built-in sorted function
        pass
    
    def set_strategy(self, strategy: Callable[[List[int]], List[int]]) -> None:
        """
        Change the sorting strategy.
        
        Args:
            strategy: New sorting function
        """
        # TODO: Set the strategy function
        pass
    
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort data using the current strategy.
        
        Args:
            data: Data to sort
            
        Returns:
            Sorted data
        """
        # TODO: Call the strategy function with data
        # TODO: Return the result
        pass

# Define function-based sorting strategies
def bubble_sort_func(data: List[int]) -> List[int]:
    """
    Bubble sort implementation as a function.
    
    Args:
        data: Data to sort
        
    Returns:
        Sorted data
    """
    # TODO: Implement bubble sort
    # TODO: Return sorted list
    pass

def quick_sort_func(data: List[int]) -> List[int]:
    """
    Quick sort implementation as a function.
    
    Args:
        data: Data to sort
        
    Returns:
        Sorted data
    """
    # TODO: Implement quick sort
    # TODO: Return sorted list
    pass

# Method 3: Strategy Pattern with Lambdas and Dictionary
class ConfigurableSorter:
    """Context class that selects strategies from a dictionary."""
    
    def __init__(self):
        # TODO: Initialize strategies dictionary with sorting functions
        # TODO: Set default strategy name
        pass
    
    def set_strategy(self, strategy_name: str) -> None:
        """
        Change the sorting strategy by name.
        
        Args:
            strategy_name: Name of the strategy to use
            
        Raises:
            KeyError: If strategy name is not found
        """
        # TODO: Check if strategy name exists
        # TODO: Set the current strategy name
        # TODO: Raise KeyError if not found
        pass
    
    def add_strategy(self, name: str, strategy: Callable[[List[int]], List[int]]) -> None:
        """
        Add a new sorting strategy.
        
        Args:
            name: Name for the strategy
            strategy: Sorting function
        """
        # TODO: Add strategy to the dictionary
        pass
    
    def sort(self, data: List[int]) -> List[int]:
        """
        Sort data using the current strategy.
        
        Args:
            data: Data to sort
            
        Returns:
            Sorted data
        """
        # TODO: Get the strategy function by name
        # TODO: Call the strategy with data
        # TODO: Return the result
        pass

# Test functions
def test_classic_strategy():
    """Test the classic strategy pattern with classes."""
    print("Testing Classic Strategy Pattern:")
    
    # Create context with default strategy
    sorter = Sorter()
    
    # Create test data
    data = [5, 3, 8, 1, 2]
    
    # Test with different strategies
    print(f"  Original data: {data}")
    
    print("  Using Bubble Sort:")
    sorter.set_strategy(BubbleSort())
    print(f"    Result: {sorter.sort(data.copy())}")
    
    print("  Using Quick Sort:")
    sorter.set_strategy(QuickSort())
    print(f"    Result: {sorter.sort(data.copy())}")
    
    print("  Using Merge Sort:")
    sorter.set_strategy(MergeSort())
    print(f"    Result: {sorter.sort(data.copy())}")

def test_functional_strategy():
    """Test the functional strategy pattern."""
    print("\nTesting Functional Strategy Pattern:")
    
    # Create context with default strategy
    sorter = FunctionalSorter()
    
    # Create test data
    data = [5, 3, 8, 1, 2]
    
    # Test with different strategies
    print(f"  Original data: {data}")
    
    print("  Using Default Sort (Python's sorted):")
    print(f"    Result: {sorter.sort(data.copy())}")
    
    print("  Using Bubble Sort Function:")
    sorter.set_strategy(bubble_sort_func)
    print(f"    Result: {sorter.sort(data.copy())}")
    
    print("  Using Quick Sort Function:")
    sorter.set_strategy(quick_sort_func)
    print(f"    Result: {sorter.sort(data.copy())}")
    
    print("  Using Lambda Expression:")
    sorter.set_strategy(lambda x: sorted(x, reverse=True))
    print(f"    Result: {sorter.sort(data.copy())}")

def test_configurable_strategy():
    """Test the configurable strategy pattern."""
    print("\nTesting Configurable Strategy Pattern:")
    
    # Create context
    sorter = ConfigurableSorter()
    
    # Create test data
    data = [5, 3, 8, 1, 2]
    
    # Test with different strategies
    print(f"  Original data: {data}")
    
    print("  Using Default Strategy:")
    print(f"    Result: {sorter.sort(data.copy())}")
    
    print("  Using 'bubble' Strategy:")
    sorter.set_strategy("bubble")
    print(f"    Result: {sorter.sort(data.copy())}")
    
    print("  Using 'quick' Strategy:")
    sorter.set_strategy("quick")
    print(f"    Result: {sorter.sort(data.copy())}")
    
    # Add custom strategy
    sorter.add_strategy("reverse", lambda x: sorted(x, reverse=True))
    print("  Using 'reverse' Strategy:")
    sorter.set_strategy("reverse")
    print(f"    Result: {sorter.sort(data.copy())}")
    
    # Try invalid strategy
    try:
        sorter.set_strategy("invalid")
    except KeyError as e:
        print(f"  Error (expected): {e}")

if __name__ == "__main__":
    # Test each strategy implementation
    test_classic_strategy()
    test_functional_strategy()
    test_configurable_strategy()
    
    # Compare approaches
    print("\nStrategy Implementation Comparison:")
    print("  1. Class-based: Traditional OOP approach with clear hierarchy")
    print("  2. Function-based: More lightweight, using functions as first-class objects")
    print("  3. Configurable: Dynamic selection of strategies by name")
    
    print("\nDiscussion:")
    print("  Which approach is more Pythonic and why?")
    print("  How does the Strategy pattern support the Open/Closed Principle?")
    print("  What are the trade-offs between these implementations?")
