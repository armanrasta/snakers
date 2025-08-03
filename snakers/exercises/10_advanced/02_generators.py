"""
Exercise 10.2: Generators and Iterators

Learn about Python generators and iterators.

Tasks:
1. Complete the generator functions below
2. Practice creating and using generators
3. Learn about iterator protocol and lazy evaluation

Topics covered:
- Generator functions (yield)
- Iterator protocol
- Lazy evaluation
- Generator expressions
- Infinite sequences
"""

from typing import Iterator, List, Dict, Any, Generator
import itertools

def count_up_to(limit: int) -> Iterator[int]:
    """
    Generate numbers from 0 up to limit.
    
    Args:
        limit: Upper limit (exclusive)
        
    Yields:
        Numbers from 0 to limit-1
        
    Example:
        >>> list(count_up_to(5))
        [0, 1, 2, 3, 4]
    """
    # TODO: Use a for loop and yield to generate numbers
    pass

def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate first n Fibonacci numbers.
    
    Args:
        n: Number of Fibonacci numbers to generate
        
    Returns:
        List of first n Fibonacci numbers
        
    Example:
        >>> fibonacci_sequence(7)
        [0, 1, 1, 2, 3, 5, 8]
    """
    # TODO: Define a generator function for Fibonacci numbers
    # TODO: Use the generator to create a list of n numbers
    pass

def generate_primes(n: int) -> List[int]:
    """
    Generate first n prime numbers.
    
    Args:
        n: Number of primes to generate
        
    Returns:
        List of first n prime numbers
        
    Example:
        >>> generate_primes(5)
        [2, 3, 5, 7, 11]
    """
    # TODO: Define a generator function for prime numbers
    # TODO: Use the generator to create a list of n primes
    pass

def file_reader(filename: str) -> Iterator[str]:
    """
    Read a file line by line (memory efficient).
    
    Args:
        filename: Path to file
        
    Yields:
        Each line from the file with whitespace stripped
        
    Example:
        >>> for line in file_reader("sample.txt"):
        ...     print(line)
    """
    # TODO: Open the file
    # TODO: Use with statement
    # TODO: Yield each line (stripped)
    pass

def chunked_list(items: List[Any], chunk_size: int) -> Iterator[List[Any]]:
    """
    Split a list into chunks of specified size.
    
    Args:
        items: List to split
        chunk_size: Size of each chunk
        
    Yields:
        Chunks of the list
        
    Example:
        >>> list(chunked_list([1, 2, 3, 4, 5, 6, 7], 3))
        [[1, 2, 3], [4, 5, 6], [7]]
    """
    # TODO: Yield chunks of the list
    # TODO: Use range() with step = chunk_size
    # TODO: Handle case when list length is not a multiple of chunk_size
    pass

def cycle_elements(items: List[Any]) -> Iterator[Any]:
    """
    Cycle through elements of a list indefinitely.
    
    Args:
        items: List to cycle through
        
    Yields:
        Elements from the list, cycling back to the beginning
        
    Example:
        >>> cycle = cycle_elements([1, 2, 3])
        >>> [next(cycle) for _ in range(7)]
        [1, 2, 3, 1, 2, 3, 1]
    """
    # TODO: Use itertools.cycle or implement your own cycling
    pass

if __name__ == "__main__":
    # Test count_up_to
    print("Counting up to 5:")
    for num in count_up_to(5):
        print(num, end=" ")
    print("\n")
    
    # Test fibonacci_sequence
    fib_nums = fibonacci_sequence(10)
    print(f"First 10 Fibonacci numbers: {fib_nums}\n")
    
    # Test generate_primes
    primes = generate_primes(10)
    print(f"First 10 prime numbers: {primes}\n")
    
    # Create a sample file for testing
    with open("sample.txt", "w") as f:
        f.write("Line 1: Hello\nLine 2: World\nLine 3: Python")
    
    # Test file_reader
    print("Reading file line by line:")
    for line in file_reader("sample.txt"):
        print(f"  {line}")
    print()
    
    # Test chunked_list
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chunks = list(chunked_list(test_list, 3))
    print(f"Chunked list: {chunks}\n")
    
    # Test cycle_elements
    print("Cycling through ['A', 'B', 'C']:")
    cycle = cycle_elements(["A", "B", "C"])
    for _ in range(8):
        print(next(cycle), end=" ")
    print()
