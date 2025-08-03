"""
Exercise 17.5: The Decorator Pattern

Learn about the Decorator design pattern and its implementation in Python.

Tasks:
1. Complete the decorator implementations below
2. Understand different ways to implement decorators
3. Apply decorators to add behavior to objects dynamically

Topics covered:
- Decorator pattern (OOP)
- Python function decorators
- Dynamic composition
- Extending behavior without subclassing
"""

from abc import ABC, abstractmethod
from functools import wraps
from typing import Callable, Any, TypeVar, cast

# Method 1: Classic OOP Decorator Pattern
class Component(ABC):
    """Abstract base class for components."""
    
    @abstractmethod
    def operation(self) -> str:
        """
        Perform the component's operation.
        
        Returns:
            Result of the operation
        """
        pass

class ConcreteComponent(Component):
    """Concrete component that can be decorated."""
    
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    """Abstract base class for decorators."""
    
    def __init__(self, component: Component):
        # TODO: Store the decorated component
        pass
    
    @abstractmethod
    def operation(self) -> str:
        """
        Perform operation, delegating to decorated component.
        
        Returns:
            Result of the operation
        """
        pass

class DecoratorA(Decorator):
    """Concrete decorator that adds behavior before the component."""
    
    def operation(self) -> str:
        # TODO: Add behavior before calling the component
        # TODO: Return modified result
        pass

class DecoratorB(Decorator):
    """Concrete decorator that adds behavior after the component."""
    
    def operation(self) -> str:
        # TODO: Call the component first
        # TODO: Add behavior after the call
        # TODO: Return modified result
        pass

# Method 2: Python Function Decorators
def logging_decorator(func: Callable) -> Callable:
    """
    Decorator that adds logging to a function.
    
    Args:
        func: Function to decorate
        
    Returns:
        Wrapped function with logging
    """
    # TODO: Define a wrapper function
    # TODO: Add logging before and after the function call
    # TODO: Return the wrapper
    pass

def repeat_decorator(times: int) -> Callable:
    """
    Decorator that repeats a function a specified number of times.
    
    Args:
        times: Number of times to repeat
        
    Returns:
        Decorator function
    """
    # TODO: Define and return the decorator function
    pass

# Method 3: Class Decorators
def add_metadata(cls):
    """
    Decorator that adds metadata to a class.
    
    Args:
        cls: Class to decorate
        
    Returns:
        Modified class
    """
    # TODO: Add a metadata dictionary to the class
    # TODO: Add methods to get and set metadata
    # TODO: Return the modified class
    pass

# Method 4: Class-based Decorators with __call__
class ExecutionTimer:
    """
    Decorator class that times function execution.
    
    Usage:
        @ExecutionTimer()
        def some_function():
            pass
    """
    
    def __init__(self, name: str = None):
        self.name = name
    
    def __call__(self, func: Callable) -> Callable:
        """
        Make the class callable as a decorator.
        
        Args:
            func: Function to decorate
            
        Returns:
            Wrapped function with timing
        """
        # TODO: Define a wrapper function
        # TODO: Add timing code before and after function call
        # TODO: Return the wrapper
        pass

# Test functions
def test_oop_decorator():
    """Test the OOP decorator pattern."""
    print("Testing OOP Decorator Pattern:")
    
    # Create a simple component
    simple = ConcreteComponent()
    print(f"  Simple component: {simple.operation()}")
    
    # Decorate with A
    decorated_a = DecoratorA(simple)
    print(f"  Decorated with A: {decorated_a.operation()}")
    
    # Decorate with B
    decorated_b = DecoratorB(simple)
    print(f"  Decorated with B: {decorated_b.operation()}")
    
    # Stack decorators
    stacked = DecoratorB(DecoratorA(simple))
    print(f"  Stacked decorators (A then B): {stacked.operation()}")

def test_function_decorators():
    """Test Python function decorators."""
    print("\nTesting Function Decorators:")
    
    @logging_decorator
    def greet(name: str) -> str:
        return f"Hello, {name}!"
    
    print("  Calling decorated function:")
    result = greet("World")
    print(f"  Result: {result}")
    
    @repeat_decorator(3)
    def countdown(start: int) -> None:
        print(f"  Countdown: {start}")
    
    print("\n  Calling function with repeat decorator:")
    countdown(5)

def test_class_decorators():
    """Test class decorators."""
    print("\nTesting Class Decorators:")
    
    @add_metadata
    class User:
        def __init__(self, name: str):
            self.name = name
        
        def greet(self) -> str:
            return f"Hello, {self.name}!"
    
    user = User("Alice")
    print(f"  User greeting: {user.greet()}")
    
    # Add metadata
    user.set_metadata("role", "admin")
    user.set_metadata("active", True)
    
    print(f"  User metadata: {user.get_metadata()}")
    print(f"  User role: {user.get_metadata('role')}")

def test_callable_class_decorators():
    """Test callable class decorators."""
    print("\nTesting Callable Class Decorators:")
    
    @ExecutionTimer("fibonacci")
    def fibonacci(n: int) -> int:
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print("  Calculating fibonacci(10):")
    result = fibonacci(10)
    print(f"  Result: {result}")

if __name__ == "__main__":
    # Test each decorator implementation
    test_oop_decorator()
    test_function_decorators()
    test_class_decorators()
    test_callable_class_decorators()
    
    # Compare approaches
    print("\nDecorator Implementation Comparison:")
    print("  1. OOP Decorator: Traditional pattern focusing on object composition")
    print("  2. Function Decorators: Pythonic way to modify function behavior")
    print("  3. Class Decorators: Modify or enhance class definitions")
    print("  4. Callable Class Decorators: Function decorators with configurable state")
    
    print("\nDiscussion:")
    print("  When would you use each type of decorator?")
    print("  How do decorators support the Open/Closed Principle?")
    print("  What are the trade-offs between OOP decorators and Python function decorators?")
