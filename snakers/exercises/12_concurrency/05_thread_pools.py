"""
Exercise 12.5: Thread Pools with concurrent.futures

Learn about using thread pools for concurrent execution in Python.

Tasks:
1. Complete the functions below
2. Learn how to use ThreadPoolExecutor
3. Understand concurrency patterns with thread pools

Topics covered:
- ThreadPoolExecutor
- Future objects
- Map and submit methods
- Callbacks and exception handling
"""

import concurrent.futures
import time
import random
import requests
from typing import List, Dict, Any, Callable

def parallel_map(func: Callable, items: List[Any], max_workers: int = 4) -> List[Any]:
    """
    Apply a function to each item in parallel using a thread pool.
    
    Args:
        func: Function to apply to each item
        items: List of items to process
        max_workers: Maximum number of worker threads
        
    Returns:
        List of results
    """
    # TODO: Create a ThreadPoolExecutor with the specified number of workers
    # TODO: Use executor.map to apply the function to all items
    # TODO: Return the results as a list
    pass

def execute_with_futures(tasks: List[Callable], max_workers: int = 4) -> List[Any]:
    """
    Execute a list of tasks concurrently using futures.
    
    Args:
        tasks: List of task functions (no arguments)
        max_workers: Maximum number of worker threads
        
    Returns:
        List of results in the order tasks were submitted
    """
    # TODO: Create a ThreadPoolExecutor
    # TODO: Submit each task and collect futures
    # TODO: Wait for all futures to complete
    # TODO: Return results in the order tasks were submitted
    pass

def process_as_completed(tasks: List[Callable], max_workers: int = 4) -> List[Dict[str, Any]]:
    """
    Process results as tasks complete, not waiting for earlier tasks.
    
    Args:
        tasks: List of task functions (no arguments)
        max_workers: Maximum number of worker threads
        
    Returns:
        List of task results with timing information in order of completion
    """
    # TODO: Create a ThreadPoolExecutor
    # TODO: Submit all tasks and collect futures
    # TODO: Use as_completed to process results as they finish
    # TODO: Return list of results with timing information in order of completion
    pass

def fetch_urls_parallel(urls: List[str], timeout: float = 5.0) -> Dict[str, Any]:
    """
    Fetch multiple URLs in parallel with timeout.
    
    Args:
        urls: List of URLs to fetch
        timeout: Timeout in seconds for each request
        
    Returns:
        Dictionary with results
    """
    results = {"successful": [], "failed": []}
    
    def fetch_url(url):
        try:
            # This can be replaced with a real HTTP request
            time.sleep(random.uniform(0.5, 7.0))  # Simulate network latency
            if random.random() < 0.2:  # 20% chance of failure
                raise requests.RequestException("Connection error")
            return {"url": url, "status": "success", "data": f"Content from {url}"}
        except requests.RequestException as e:
            return {"url": url, "status": "error", "error": str(e)}
    
    # TODO: Create a ThreadPoolExecutor
    # TODO: Submit fetch_url for each URL with the timeout
    # TODO: Process results, separating successful and failed requests
    # TODO: Return the results dictionary
    pass

def parallel_map_with_progress(func: Callable, items: List[Any], max_workers: int = 4) -> List[Any]:
    """
    Apply a function to items in parallel with progress tracking.
    
    Args:
        func: Function to apply to each item
        items: List of items to process
        max_workers: Maximum number of worker threads
        
    Returns:
        List of results
    """
    results = []
    completed = 0
    total = len(items)
    
    def progress_callback(future):
        nonlocal completed
        completed += 1
        print(f"Progress: {completed}/{total} tasks completed ({completed/total:.1%})")
    
    # TODO: Create a ThreadPoolExecutor
    # TODO: Submit each task and add a callback for progress tracking
    # TODO: Wait for all tasks to complete
    # TODO: Return the results
    pass

if __name__ == "__main__":
    # Test parallel map
    def square(x):
        time.sleep(0.1)  # Simulate computation
        return x * x
    
    print("Testing parallel map:")
    numbers = list(range(1, 11))
    start = time.time()
    squared = parallel_map(square, numbers)
    elapsed = time.time() - start
    print(f"Results: {squared}")
    print(f"Time taken: {elapsed:.2f}s")
    
    # Test executing with futures
    def task(task_id):
        sleep_time = random.uniform(0.5, 1.5)
        time.sleep(sleep_time)
        return {"task_id": task_id, "sleep_time": sleep_time}
    
    print("\nTesting execute with futures:")
    tasks = [lambda i=i: task(i) for i in range(1, 6)]
    results = execute_with_futures(tasks)
    for result in results:
        print(f"Task {result['task_id']}: slept for {result['sleep_time']:.2f}s")
    
    # Test process as completed
    print("\nTesting process as completed:")
    tasks = [lambda i=i: task(i) for i in range(1, 6)]
    results = process_as_completed(tasks)
    for result in results:
        print(f"Task {result['result']['task_id']} completed in {result['time']:.2f}s")
    
    # Test URL fetching
    print("\nTesting parallel URL fetching:")
    urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3",
        "https://example.com/page4",
        "https://example.com/page5",
    ]
    fetch_results = fetch_urls_parallel(urls)
    print(f"Successful: {len(fetch_results['successful'])}")
    print(f"Failed: {len(fetch_results['failed'])}")
    
    # Test parallel map with progress
    print("\nTesting parallel map with progress:")
    def slow_square(x):
        time.sleep(0.5)  # Longer task to see progress
        return x * x
    
    numbers = list(range(1, 11))
    results = parallel_map_with_progress(slow_square, numbers)
    print(f"Final results: {results}")
