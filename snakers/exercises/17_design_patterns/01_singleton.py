"""
Exercise 17.1: The Singleton Pattern

Learn about the Singleton design pattern and its implementation in Python.

Tasks:
1. Complete the singleton implementations below
2. Understand different ways to create singletons in Python
3. Compare the benefits and drawbacks of each approach

Topics covered:
- Singleton design pattern
- Class decorators
- Metaclasses
- Module-level singletons
"""

from typing import Dict, Any, Type, TypeVar, cast

# Method 1: Basic implementation with instance checking
class BasicSingleton:
    """A basic singleton implementation."""
    
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        # TODO: Check if _instance exists
        # TODO: Create instance if it doesn't exist
        # TODO: Return the instance
        pass
    
    def __init__(self, value: str = ""):
        # Initialize attributes only once
        # TODO: Set self.value only if it doesn't exist
        pass

# Method 2: Singleton using a decorator
def singleton_decorator(cls):
    """
    A decorator that converts a class into a singleton.
    
    Args:
        cls: Class to convert to singleton
        
    Returns:
        Singleton class
    """
    # TODO: Create an instances dictionary
    # TODO: Define a get_instance wrapper function
    # TODO: Return the wrapper
    pass

@singleton_decorator
class DecoratedSingleton:
    """A singleton implemented using a decorator."""
    
    def __init__(self, value: str = ""):
        self.value = value

# Method 3: Singleton using a metaclass
class SingletonMeta(type):
    """A metaclass that creates singleton classes."""
    
    _instances: Dict[Type, Any] = {}
    
    def __call__(cls, *args, **kwargs):
        # TODO: Check if class exists in _instances
        # TODO: Create instance if it doesn't exist
        # TODO: Return the instance
        pass

class MetaSingleton(metaclass=SingletonMeta):
    """A singleton implemented using a metaclass."""
    
    def __init__(self, value: str = ""):
        self.value = value

# Method 4: Borg pattern (shared state)
class BorgSingleton:
    """
    A singleton-like pattern that shares state between instances.
    This is sometimes called the "Monostate" pattern.
    """
    
    _shared_state: Dict[str, Any] = {}
    
    def __init__(self, value: str = ""):
        # TODO: Set __dict__ to point to _shared_state
        # TODO: Set value attribute
        pass

# Test functions
def test_singleton(singleton_class) -> bool:
    """
    Test if a class is truly a singleton.
    
    Args:
        singleton_class: Class to test
        
    Returns:
        True if singleton, False otherwise
    """
    instance1 = singleton_class("First")
    instance2 = singleton_class("Second")
    
    # Check instance identity
    identical_instances = instance1 is instance2
    
    # Check attribute values
    same_value = instance1.value == instance2.value
    
    print(f"Testing {singleton_class.__name__}:")
    print(f"  Identical instances: {identical_instances}")
    print(f"  Same value: {same_value}")
    print(f"  Value: {instance1.value}")
    
    return identical_instances

if __name__ == "__main__":
    # Test each singleton implementation
    test_singleton(BasicSingleton)
    test_singleton(DecoratedSingleton)
    test_singleton(MetaSingleton)
    
    # The Borg pattern is different - instances are different but share state
    borg1 = BorgSingleton("Borg Value")
    borg2 = BorgSingleton("New Value")
    
    print("\nTesting BorgSingleton:")
    print(f"  Identical instances: {borg1 is borg2}")
    print(f"  Same value: {borg1.value == borg2.value}")
    print(f"  Values: {borg1.value}, {borg2.value}")
    
    # Compare approaches
    print("\nSingleton Implementation Comparison:")
    print("  1. Basic Singleton: Simple but requires custom __new__ method")
    print("  2. Decorated Singleton: Clean and reusable but adds a wrapper layer")
    print("  3. Metaclass Singleton: Powerful but more complex")
    print("  4. Borg Pattern: Focuses on shared state rather than identity")
    
    print("\nDiscussion:")
    print("  Which approach do you prefer and why?")
    print("  What are the trade-offs between these implementations?")
    print("  When would you use a singleton in a real project?")
