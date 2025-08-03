"""
Exercise 12.4: Synchronization Primitives

Learn about synchronization primitives in Python's threading and multiprocessing modules.

Tasks:
1. Complete the functions below
2. Learn how to use different synchronization primitives
3. Understand race conditions and deadlocks

Topics covered:
- Locks and RLocks
- Semaphores
- Conditions
- Events
- Barriers
"""

import threading
import time
import random
from typing import List, Dict, Any

def demonstrate_lock() -> Dict[str, Any]:
    """
    Demonstrate the usage of threading.Lock.
    
    Returns:
        Dictionary with results and timing
    """
    shared_resource = []
    
    # TODO: Create a lock object
    
    def add_without_lock():
        for i in range(100):
            # Simulate race condition without a lock
            current = len(shared_resource)
            time.sleep(0.001)  # Small delay to increase chance of race condition
            shared_resource.append(current)
    
    def add_with_lock():
        for i in range(100):
            # TODO: Acquire the lock
            # TODO: Add the current length to the shared resource
            # TODO: Release the lock
            pass
    
    # Test without lock
    shared_resource.clear()
    threads = [threading.Thread(target=add_without_lock) for _ in range(5)]
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    no_lock_time = time.time() - start
    no_lock_result = shared_resource.copy()
    
    # Test with lock
    shared_resource.clear()
    threads = [threading.Thread(target=add_with_lock) for _ in range(5)]
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    with_lock_time = time.time() - start
    with_lock_result = shared_resource.copy()
    
    return {
        "without_lock": {
            "result": no_lock_result,
            "is_sequential": no_lock_result == list(range(500)),
            "time": no_lock_time
        },
        "with_lock": {
            "result": with_lock_result,
            "is_sequential": with_lock_result == list(range(500)),
            "time": with_lock_time
        }
    }

def demonstrate_semaphore() -> Dict[str, Any]:
    """
    Demonstrate the usage of threading.Semaphore for limiting concurrency.
    
    Returns:
        Dictionary with execution results
    """
    results = []
    
    # TODO: Create a semaphore that allows 3 concurrent threads
    
    def worker(worker_id):
        # TODO: Acquire the semaphore
        results.append(f"Worker {worker_id} started")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate work
        results.append(f"Worker {worker_id} finished")
        # TODO: Release the semaphore
    
    # TODO: Create and start 10 worker threads
    # TODO: Wait for all threads to complete
    
    return {
        "execution_log": results,
        "max_concurrent": 3  # This should match your semaphore value
    }

def demonstrate_condition() -> Dict[str, List[str]]:
    """
    Demonstrate the usage of threading.Condition for producer-consumer pattern.
    
    Returns:
        Dictionary with producer and consumer logs
    """
    buffer = []
    MAX_SIZE = 5
    producer_log = []
    consumer_log = []
    
    # TODO: Create a condition variable
    
    def producer():
        for i in range(10):
            # TODO: Acquire the condition
            # TODO: Wait if buffer is full
            # TODO: Add item to buffer
            # TODO: Log the action
            # TODO: Notify consumers
            # TODO: Release the condition
            time.sleep(random.uniform(0.1, 0.3))  # Simulate work
    
    def consumer():
        for i in range(5):  # Each consumer consumes 5 items
            # TODO: Acquire the condition
            # TODO: Wait if buffer is empty
            # TODO: Remove item from buffer
            # TODO: Log the action
            # TODO: Notify producers
            # TODO: Release the condition
            time.sleep(random.uniform(0.2, 0.5))  # Simulate work
    
    # TODO: Create and start producer and consumer threads
    # TODO: Wait for all threads to complete
    
    return {
        "producer_log": producer_log,
        "consumer_log": consumer_log
    }

def demonstrate_event() -> Dict[str, List[str]]:
    """
    Demonstrate the usage of threading.Event for signaling between threads.
    
    Returns:
        Dictionary with worker logs
    """
    logs = []
    
    # TODO: Create an event object
    
    def waiter(worker_id):
        logs.append(f"Worker {worker_id} waiting for event")
        # TODO: Wait for the event to be set
        logs.append(f"Worker {worker_id} received event, continuing execution")
    
    def setter():
        logs.append("Main thread sleeping before setting event")
        time.sleep(2)  # Sleep for 2 seconds
        logs.append("Main thread setting event")
        # TODO: Set the event
    
    # TODO: Create and start waiter threads
    # TODO: Create and start setter thread
    # TODO: Wait for all threads to complete
    
    return {"logs": logs}

def demonstrate_barrier() -> Dict[str, List[str]]:
    """
    Demonstrate the usage of threading.Barrier for synchronizing threads.
    
    Returns:
        Dictionary with worker logs
    """
    logs = []
    
    # TODO: Create a barrier for 4 threads
    
    def worker(worker_id):
        logs.append(f"Worker {worker_id} started and working")
        time.sleep(random.uniform(0.5, 2.0))  # Simulate different work times
        logs.append(f"Worker {worker_id} reached the barrier")
        # TODO: Wait at the barrier
        logs.append(f"Worker {worker_id} continued after the barrier")
    
    # TODO: Create and start worker threads
    # TODO: Wait for all threads to complete
    
    return {"logs": logs}

if __name__ == "__main__":
    # Test lock
    print("Testing Lock:")
    lock_results = demonstrate_lock()
    print(f"Without lock sequential: {lock_results['without_lock']['is_sequential']}")
    print(f"With lock sequential: {lock_results['with_lock']['is_sequential']}")
    print(f"Without lock time: {lock_results['without_lock']['time']:.4f}s")
    print(f"With lock time: {lock_results['with_lock']['time']:.4f}s")
    
    # Test semaphore
    print("\nTesting Semaphore:")
    semaphore_results = demonstrate_semaphore()
    print("Execution log:")
    for entry in semaphore_results["execution_log"]:
        print(f"  {entry}")
    
    # Test condition
    print("\nTesting Condition:")
    condition_results = demonstrate_condition()
    print("Producer log:")
    for entry in condition_results["producer_log"]:
        print(f"  {entry}")
    print("Consumer log:")
    for entry in condition_results["consumer_log"]:
        print(f"  {entry}")
    
    # Test event
    print("\nTesting Event:")
    event_results = demonstrate_event()
    for entry in event_results["logs"]:
        print(f"  {entry}")
    
    # Test barrier
    print("\nTesting Barrier:")
    barrier_results = demonstrate_barrier()
    for entry in barrier_results["logs"]:
        print(f"  {entry}")
