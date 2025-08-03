"""
Exercise 12.1: Threading Basics

Learn about Python's threading module and basic thread operations.

Tasks:
1. Complete the functions below
2. Learn how to create and manage threads
3. Understand thread synchronization and shared data

Topics covered:
- Thread creation and management
- Thread arguments and naming
- Thread lifecycle
- Thread safety considerations
"""

import threading
import time
from typing import List, Callable, Any

def create_and_run_thread(target_function: Callable, args: tuple = ()) -> threading.Thread:
    """
    Create and start a new thread that executes the given function.
    
    Args:
        target_function: Function to execute in the thread
        args: Arguments to pass to the function
        
    Returns:
        The started thread object
    """
    # TODO: Create a thread with the target function and arguments
    # TODO: Start the thread
    # TODO: Return the thread object
    pass

def run_multiple_threads(target_function: Callable, num_threads: int) -> List[threading.Thread]:
    """
    Create and start multiple threads running the same function.
    
    Args:
        target_function: Function to execute in the threads
        num_threads: Number of threads to create
        
    Returns:
        List of started thread objects
    """
    # TODO: Create a list to store threads
    # TODO: Create and start 'num_threads' threads with the target function
    # TODO: Return the list of threads
    pass

def wait_for_threads(threads: List[threading.Thread]) -> None:
    """
    Wait for all threads in the list to complete.
    
    Args:
        threads: List of thread objects to wait for
    """
    # TODO: Join each thread in the list to wait for completion
    pass

def demonstrate_race_condition() -> List[int]:
    """
    Demonstrate a race condition with multiple threads.
    
    Returns:
        The final counter value after all threads have executed
    """
    counter = [0]  # Using a list for a mutable object
    
    def increment():
        # Read current value
        current = counter[0]
        # Simulate some processing time
        time.sleep(0.001)
        # Write updated value
        counter[0] = current + 1
    
    # TODO: Create and start 10 threads that all call increment()
    # TODO: Wait for all threads to complete
    # TODO: Return the final counter value
    pass

def fix_race_condition() -> int:
    """
    Fix the race condition using a threading.Lock.
    
    Returns:
        The final counter value after all threads have executed
    """
    counter = [0]
    lock = threading.Lock()
    
    def safe_increment():
        # TODO: Acquire the lock before updating the counter
        # TODO: Update the counter safely
        # TODO: Release the lock after updating
        pass
    
    # TODO: Create and start 10 threads that all call safe_increment()
    # TODO: Wait for all threads to complete
    # TODO: Return the final counter value
    pass

def execute_with_timeout(func: Callable, timeout: float) -> Any:
    """
    Execute a function with a timeout.
    
    Args:
        func: Function to execute
        timeout: Maximum time to wait (in seconds)
        
    Returns:
        Result of the function or None if it times out
    """
    result = [None]
    
    def worker():
        result[0] = func()
    
    # TODO: Create a thread for the worker function
    # TODO: Start the thread and wait for completion with a timeout
    # TODO: Return the result or None if timeout occurs
    pass

if __name__ == "__main__":
    # Test basic thread creation
    def say_hello(name):
        time.sleep(0.1)
        print(f"Hello from thread! I'm {name}")
    
    thread = create_and_run_thread(say_hello, ("Thread 1",))
    thread.join()
    
    # Test multiple threads
    def count_to_three(thread_id):
        for i in range(1, 4):
            print(f"Thread {thread_id}: {i}")
            time.sleep(0.1)
    
    threads = run_multiple_threads(lambda: count_to_three("A"), 3)
    wait_for_threads(threads)
    
    # Test race condition
    print("\nRace condition demonstration:")
    final_count = demonstrate_race_condition()
    print(f"Final count with race condition: {final_count}")
    
    # Test fixed race condition
    print("\nFixed race condition:")
    final_count = fix_race_condition()
    print(f"Final count with lock: {final_count}")
    
    # Test timeout
    def slow_function():
        time.sleep(2)
        return "Completed"
    
    print("\nTesting function timeout:")
    result = execute_with_timeout(slow_function, 1.0)
    print(f"Result with 1s timeout: {result}")
    
    result = execute_with_timeout(slow_function, 3.0)
    print(f"Result with 3s timeout: {result}")
