"""
Exercise 17.2: The Factory Pattern

Learn about the Factory design pattern and its implementation in Python.

Tasks:
1. Complete the factory implementations below
2. Understand different factory pattern variations
3. Apply factories to create objects without specifying exact classes

Topics covered:
- Factory Method pattern
- Abstract Factory pattern
- Factory function implementation
- Class registration
"""

from abc import ABC, abstractmethod
from typing import Dict, Type, Any, Callable, Optional

# Basic product classes
class Animal(ABC):
    """Abstract base class for animals."""
    
    @abstractmethod
    def speak(self) -> str:
        """Return the sound the animal makes."""
        pass

class Dog(Animal):
    """A concrete animal implementation."""
    
    def speak(self) -> str:
        return "Woof!"

class Cat(Animal):
    """A concrete animal implementation."""
    
    def speak(self) -> str:
        return "Meow!"

class Duck(Animal):
    """A concrete animal implementation."""
    
    def speak(self) -> str:
        return "Quack!"

# Method 1: Simple Factory Function
def animal_factory(animal_type: str) -> Animal:
    """
    A simple factory function that creates animals.
    
    Args:
        animal_type: Type of animal to create ("dog", "cat", "duck")
        
    Returns:
        An Animal instance
        
    Raises:
        ValueError: If animal_type is not recognized
    """
    # TODO: Implement the factory function using a dictionary or if/elif/else
    # TODO: Return appropriate Animal subclass instance based on animal_type
    # TODO: Raise ValueError for unknown animal types
    pass

# Method 2: Factory Method Pattern
class AnimalFactory(ABC):
    """Abstract factory base class."""
    
    @abstractmethod
    def create_animal(self) -> Animal:
        """Create and return an animal."""
        pass

class DogFactory(AnimalFactory):
    """Factory for creating dogs."""
    
    # TODO: Implement create_animal to return a Dog
    pass

class CatFactory(AnimalFactory):
    """Factory for creating cats."""
    
    # TODO: Implement create_animal to return a Cat
    pass

class DuckFactory(AnimalFactory):
    """Factory for creating ducks."""
    
    # TODO: Implement create_animal to return a Duck
    pass

# Method 3: Factory with Registration
class FactoryRegistry:
    """A factory that registers and creates objects by name."""
    
    def __init__(self):
        # TODO: Initialize a dictionary to store registered classes
        pass
    
    def register(self, key: str, cls: Type) -> None:
        """
        Register a class with a key.
        
        Args:
            key: The key to register the class under
            cls: The class to register
        """
        # TODO: Add the class to the registry
        pass
    
    def create(self, key: str, *args, **kwargs) -> Any:
        """
        Create an instance of a registered class.
        
        Args:
            key: The key the class is registered under
            *args: Positional arguments to pass to the constructor
            **kwargs: Keyword arguments to pass to the constructor
            
        Returns:
            Instance of the registered class
            
        Raises:
            KeyError: If key is not registered
        """
        # TODO: Get the class from the registry
        # TODO: Create and return an instance
        # TODO: Raise KeyError if key is not registered
        pass

# Method 4: Abstract Factory Pattern
class Environment(ABC):
    """An abstract factory for creating related objects."""
    
    @abstractmethod
    def create_food(self) -> str:
        """Create food appropriate for the environment."""
        pass
    
    @abstractmethod
    def create_habitat(self) -> str:
        """Create habitat appropriate for the environment."""
        pass
    
    @abstractmethod
    def create_animal(self) -> Animal:
        """Create animal appropriate for the environment."""
        pass

class ForestEnvironment(Environment):
    """A concrete factory for forest environments."""
    
    # TODO: Implement create_food to return "berries"
    # TODO: Implement create_habitat to return "trees"
    # TODO: Implement create_animal to return a Dog
    pass

class OceanEnvironment(Environment):
    """A concrete factory for ocean environments."""
    
    # TODO: Implement create_food to return "fish"
    # TODO: Implement create_habitat to return "water"
    # TODO: Implement create_animal to return a Duck
    pass

# Test functions
def test_simple_factory():
    """Test the simple factory function."""
    animals = ["dog", "cat", "duck"]
    
    print("Testing Simple Factory:")
    for animal_type in animals:
        animal = animal_factory(animal_type)
        print(f"  {animal_type.capitalize()}: {animal.speak()}")
    
    try:
        animal_factory("elephant")
    except ValueError as e:
        print(f"  Error (expected): {e}")

def test_factory_method():
    """Test the factory method pattern."""
    factories = [DogFactory(), CatFactory(), DuckFactory()]
    
    print("\nTesting Factory Method:")
    for factory in factories:
        animal = factory.create_animal()
        print(f"  {factory.__class__.__name__}: {animal.speak()}")

def test_registry_factory():
    """Test the registry factory."""
    registry = FactoryRegistry()
    registry.register("dog", Dog)
    registry.register("cat", Cat)
    registry.register("duck", Duck)
    
    print("\nTesting Registry Factory:")
    for animal_type in ["dog", "cat", "duck"]:
        animal = registry.create(animal_type)
        print(f"  {animal_type.capitalize()}: {animal.speak()}")
    
    try:
        registry.create("elephant")
    except KeyError as e:
        print(f"  Error (expected): {e}")

def test_abstract_factory():
    """Test the abstract factory pattern."""
    environments = [ForestEnvironment(), OceanEnvironment()]
    
    print("\nTesting Abstract Factory:")
    for env in environments:
        food = env.create_food()
        habitat = env.create_habitat()
        animal = env.create_animal()
        
        print(f"  {env.__class__.__name__}:")
        print(f"    Food: {food}")
        print(f"    Habitat: {habitat}")
        print(f"    Animal sound: {animal.speak()}")

if __name__ == "__main__":
    # Test each factory implementation
    test_simple_factory()
    test_factory_method()
    test_registry_factory()
    test_abstract_factory()
    
    # Compare approaches
    print("\nFactory Implementation Comparison:")
    print("  1. Simple Factory: Easy to use but limited extensibility")
    print("  2. Factory Method: Good for inheritance hierarchies")
    print("  3. Registry Factory: Flexible, allows dynamic registration")
    print("  4. Abstract Factory: Creates families of related objects")
    
    print("\nDiscussion:")
    print("  Which approach is best for your current project?")
    print("  How would you extend these patterns for more complex scenarios?")
    print("  What are the trade-offs between flexibility and complexity?")
