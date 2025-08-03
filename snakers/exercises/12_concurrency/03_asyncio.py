"""
Exercise 12.3: Asynchronous Programming with asyncio

Learn about Python's asyncio module for asynchronous programming.

Tasks:
1. Complete the coroutines below
2. Learn how to use async/await syntax
3. Understand asynchronous execution and event loops

Topics covered:
- Coroutines with async/await
- Task creation and management
- Asynchronous I/O operations
- Event loops
"""

import asyncio
import time
from typing import List, Dict, Any

async def simple_coroutine() -> str:
    """
    A simple coroutine that waits and returns a message.
    
    Returns:
        A greeting message
    """
    # TODO: Use asyncio.sleep() to simulate a non-blocking wait
    # TODO: Return a greeting message
    pass

async def run_in_sequence(tasks: List[int]) -> float:
    """
    Run a list of sleep tasks in sequence.
    
    Args:
        tasks: List of sleep durations in seconds
        
    Returns:
        Total time taken
    """
    start = time.time()
    
    # TODO: Iterate through each task duration
    # TODO: For each duration, await asyncio.sleep(duration)
    
    return time.time() - start

async def run_concurrently(tasks: List[int]) -> float:
    """
    Run a list of sleep tasks concurrently.
    
    Args:
        tasks: List of sleep durations in seconds
        
    Returns:
        Total time taken
    """
    start = time.time()
    
    # TODO: Create a list of asyncio.create_task() for each sleep duration
    # TODO: Await all tasks using asyncio.gather()
    
    return time.time() - start

async def fetch_data(url: str, timeout: float = 5.0) -> Dict[str, Any]:
    """
    Simulate fetching data from a URL with timeout.
    
    Args:
        url: URL to fetch data from
        timeout: Maximum time to wait
        
    Returns:
        Dictionary with fetch result
        
    Note: This is a simulation and doesn't actually make HTTP requests
    """
    # Simulate different response times based on URL
    if "fast" in url:
        delay = 1.0
    elif "medium" in url:
        delay = 3.0
    else:
        delay = 6.0  # Will exceed default timeout
    
    # TODO: Create a try/except block to handle TimeoutError
    # TODO: Use asyncio.wait_for() with the given timeout
    # TODO: Return success result if completed or timeout message if timed out
    pass

async def process_data_as_available(urls: List[str]) -> List[Dict[str, Any]]:
    """
    Process data from URLs as it becomes available.
    
    Args:
        urls: List of URLs to fetch data from
        
    Returns:
        List of results in order of completion
    """
    # TODO: Create a list of fetch_data tasks
    # TODO: Use asyncio.as_completed to process results as they arrive
    # TODO: Return list of results in order of completion
    pass

async def handle_cancellation() -> str:
    """
    Demonstrate task cancellation.
    
    Returns:
        Status message
    """
    try:
        # TODO: Create a long-running coroutine
        # TODO: Create a task for this coroutine
        # TODO: Sleep briefly, then cancel the task
        # TODO: Try to await the task and handle CancelledError
        # TODO: Return success message
        pass
    except asyncio.CancelledError:
        return "Task cancellation was not handled properly"

async def run_with_timeout(coro, timeout: float):
    """
    Run a coroutine with a timeout.
    
    Args:
        coro: Coroutine to run
        timeout: Maximum time to wait
        
    Returns:
        Coroutine result or timeout message
    """
    # TODO: Use asyncio.wait_for() to run the coroutine with a timeout
    # TODO: Handle TimeoutError and return appropriate message
    pass

if __name__ == "__main__":
    # Run all tests using asyncio.run()
    async def main():
        # Test simple coroutine
        result = await simple_coroutine()
        print(f"Simple coroutine result: {result}")
        
        # Compare sequential vs concurrent execution
        tasks = [1, 1, 1, 1]
        
        seq_time = await run_in_sequence(tasks)
        print(f"\nSequential execution time: {seq_time:.2f}s")
        
        con_time = await run_concurrently(tasks)
        print(f"Concurrent execution time: {con_time:.2f}s")
        print(f"Speed improvement: {seq_time / con_time:.1f}x")
        
        # Test fetch with timeout
        print("\nTesting fetch with timeout:")
        fast_result = await fetch_data("https://example.com/fast")
        print(f"Fast URL result: {fast_result}")
        
        slow_result = await fetch_data("https://example.com/slow")
        print(f"Slow URL result: {slow_result}")
        
        # Test processing as available
        print("\nProcessing URLs as they complete:")
        urls = [
            "https://example.com/medium",
            "https://example.com/fast",
            "https://example.com/slow",
        ]
        results = await process_data_as_available(urls)
        for i, result in enumerate(results):
            print(f"Result {i+1}: {result}")
        
        # Test cancellation
        print("\nTesting task cancellation:")
        cancel_result = await handle_cancellation()
        print(f"Cancellation result: {cancel_result}")
        
        # Test timeout wrapper
        print("\nTesting timeout wrapper:")
        async def slow_operation():
            await asyncio.sleep(3)
            return "Completed"
        
        timeout_result = await run_with_timeout(slow_operation(), 1.0)
        print(f"Timeout result (1s timeout): {timeout_result}")
        
        normal_result = await run_with_timeout(slow_operation(), 5.0)
        print(f"Normal result (5s timeout): {normal_result}")
    
    asyncio.run(main())
