"""
Exercise 12.2: Multiprocessing Basics

Learn about Python's multiprocessing module for parallel execution.

Tasks:
1. Complete the functions below
2. Learn how to create and manage processes
3. Understand inter-process communication

Topics covered:
- Process creation and management
- Process pools
- Shared memory and queues
- Process vs threading considerations
"""

import multiprocessing as mp
import time
import os
from typing import List, Callable, Any

def create_and_run_process(target_function: Callable, args: tuple = ()) -> mp.Process:
    """
    Create and start a new process that executes the given function.
    
    Args:
        target_function: Function to execute in the process
        args: Arguments to pass to the function
        
    Returns:
        The started process object
    """
    # TODO: Create a process with the target function and arguments
    # TODO: Start the process
    # TODO: Return the process object
    pass

def run_multiple_processes(target_function: Callable, num_processes: int) -> List[mp.Process]:
    """
    Create and start multiple processes running the same function.
    
    Args:
        target_function: Function to execute in the processes
        num_processes: Number of processes to create
        
    Returns:
        List of started process objects
    """
    # TODO: Create a list to store processes
    # TODO: Create and start 'num_processes' processes with the target function
    # TODO: Return the list of processes
    pass

def wait_for_processes(processes: List[mp.Process]) -> None:
    """
    Wait for all processes in the list to complete.
    
    Args:
        processes: List of process objects to wait for
    """
    # TODO: Join each process in the list to wait for completion
    pass

def calculate_sum_with_processes(numbers: List[int], num_processes: int) -> int:
    """
    Calculate the sum of numbers using multiple processes.
    
    Args:
        numbers: List of numbers to sum
        num_processes: Number of processes to use
        
    Returns:
        Sum of all numbers
    """
    # Calculate chunk size for dividing the work
    chunk_size = len(numbers) // num_processes
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    # Create a shared value to store the result
    result = mp.Value('i', 0)
    
    def process_chunk(chunk, shared_result):
        # TODO: Calculate the sum of the chunk
        # TODO: Add the sum to the shared result using a lock
        pass
    
    # TODO: Create and start a process for each chunk
    # TODO: Wait for all processes to complete
    # TODO: Return the final sum from the shared result
    pass

def communicate_with_queue() -> List[int]:
    """
    Demonstrate inter-process communication with a queue.
    
    Returns:
        List of received values
    """
    # Create a queue for communication
    queue = mp.Queue()
    
    def producer():
        # TODO: Put 5 numbers into the queue
        # TODO: Put a sentinel value to indicate completion
        pass
    
    def consumer(q, results):
        # TODO: Read values from the queue until sentinel is received
        # TODO: Append each value to the results list
        pass
    
    # Create shared list for results
    manager = mp.Manager()
    results = manager.list()
    
    # TODO: Create and start producer and consumer processes
    # TODO: Wait for both processes to complete
    # TODO: Return the results as a normal Python list
    pass

def parallel_map(func: Callable, items: List[Any], num_processes: int) -> List[Any]:
    """
    Apply a function to each item in parallel using multiple processes.
    
    Args:
        func: Function to apply to each item
        items: List of items to process
        num_processes: Number of processes to use
        
    Returns:
        List of results from applying the function to each item
    """
    # TODO: Create a process pool with the specified number of processes
    # TODO: Use the pool to map the function to each item
    # TODO: Close the pool and wait for completion
    # TODO: Return the results
    pass

if __name__ == "__main__":
    # Test basic process creation
    def show_process_info():
        print(f"Process ID: {os.getpid()}, Parent ID: {os.getppid()}")
    
    process = create_and_run_process(show_process_info)
    process.join()
    
    # Test multiple processes
    processes = run_multiple_processes(show_process_info, 3)
    wait_for_processes(processes)
    
    # Test sum calculation
    numbers = list(range(1, 1001))
    start = time.time()
    total = sum(numbers)
    print(f"\nSequential sum: {total}, Time: {time.time() - start:.4f}s")
    
    start = time.time()
    parallel_total = calculate_sum_with_processes(numbers, 4)
    print(f"Parallel sum: {parallel_total}, Time: {time.time() - start:.4f}s")
    
    # Test queue communication
    print("\nTesting queue communication:")
    results = communicate_with_queue()
    print(f"Received values: {results}")
    
    # Test parallel map
    def square(x):
        return x * x
    
    numbers = list(range(1, 11))
    print("\nTesting parallel map:")
    squared = parallel_map(square, numbers, 4)
    print(f"Squared numbers: {squared}")
