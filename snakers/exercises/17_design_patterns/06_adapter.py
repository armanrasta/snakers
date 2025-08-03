"""
Exercise 17.6: The Adapter Pattern

Learn about the Adapter design pattern and its implementation in Python.

Tasks:
1. Complete the adapter implementations below
2. Understand different approaches to creating adapters
3. Apply adapters to make incompatible interfaces work together

Topics covered:
- Adapter pattern (object and class)
- Interface compatibility
- Legacy code integration
- Object composition vs. inheritance
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Any

# Legacy system with incompatible interface
class LegacyRectangle:
    """A legacy rectangle class with incompatible interface."""
    
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def get_coordinates(self) -> Dict[str, float]:
        """Get rectangle coordinates."""
        return {
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2
        }

# Target interface
class Shape(ABC):
    """Target interface for all shapes."""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate shape area."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate shape perimeter."""
        pass
    
    @abstractmethod
    def describe(self) -> str:
        """Get shape description."""
        pass

class Circle(Shape):
    """A circle implementing the Shape interface."""
    
    def __init__(self, center_x: float, center_y: float, radius: float):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
    
    def area(self) -> float:
        """Calculate circle area."""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """Calculate circle circumference."""
        import math
        return 2 * math.pi * self.radius
    
    def describe(self) -> str:
        """Get circle description."""
        return f"Circle at ({self.center_x}, {self.center_y}) with radius {self.radius}"

# Method 1: Object Adapter Pattern
class RectangleAdapter(Shape):
    """
    Adapter for LegacyRectangle to make it compatible with Shape interface.
    This uses object composition.
    """
    
    def __init__(self, legacy_rectangle: LegacyRectangle):
        # TODO: Store the adaptee
        pass
    
    def area(self) -> float:
        """
        Calculate rectangle area.
        
        Returns:
            Rectangle area
        """
        # TODO: Get coordinates from legacy rectangle
        # TODO: Calculate and return the area
        pass
    
    def perimeter(self) -> float:
        """
        Calculate rectangle perimeter.
        
        Returns:
            Rectangle perimeter
        """
        # TODO: Get coordinates from legacy rectangle
        # TODO: Calculate and return the perimeter
        pass
    
    def describe(self) -> str:
        """
        Get rectangle description.
        
        Returns:
            Rectangle description
        """
        # TODO: Get coordinates from legacy rectangle
        # TODO: Return formatted description
        pass

# Method 2: Class Adapter Pattern (using inheritance)
class RectangleClassAdapter(LegacyRectangle, Shape):
    """
    Adapter for LegacyRectangle using inheritance.
    This inherits from both the adaptee and target.
    """
    
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        # TODO: Initialize the parent class
        pass
    
    def area(self) -> float:
        """
        Calculate rectangle area.
        
        Returns:
            Rectangle area
        """
        # TODO: Calculate and return the area
        pass
    
    def perimeter(self) -> float:
        """
        Calculate rectangle perimeter.
        
        Returns:
            Rectangle perimeter
        """
        # TODO: Calculate and return the perimeter
        pass
    
    def describe(self) -> str:
        """
        Get rectangle description.
        
        Returns:
            Rectangle description
        """
        # TODO: Return formatted description
        pass

# Method 3: Function-based Adapter
def shape_adapter(obj: Any) -> Shape:
    """
    Create a Shape adapter for various objects.
    
    Args:
        obj: Object to adapt
        
    Returns:
        Shape compatible object
        
    Raises:
        TypeError: If obj cannot be adapted to Shape
    """
    # TODO: Check if obj is already a Shape
    # TODO: If obj is a LegacyRectangle, return a RectangleAdapter
    # TODO: Handle other potential object types that could be adapted
    # TODO: Raise TypeError if object cannot be adapted
    pass

# Method 4: Duck Typing Adapter (Pythonic approach)
class DuckTypingRectangle:
    """
    Duck typing adapter that doesn't explicitly inherit from Shape.
    It just implements the required methods.
    """
    
    def __init__(self, legacy_rectangle: LegacyRectangle):
        # TODO: Store the legacy rectangle
        pass
    
    def area(self) -> float:
        """
        Calculate rectangle area.
        
        Returns:
            Rectangle area
        """
        # TODO: Get coordinates from legacy rectangle
        # TODO: Calculate and return the area
        pass
    
    def perimeter(self) -> float:
        """
        Calculate rectangle perimeter.
        
        Returns:
            Rectangle perimeter
        """
        # TODO: Get coordinates from legacy rectangle
        # TODO: Calculate and return the perimeter
        pass
    
    def describe(self) -> str:
        """
        Get rectangle description.
        
        Returns:
            Rectangle description
        """
        # TODO: Get coordinates from legacy rectangle
        # TODO: Return formatted description
        pass

# Test functions
def test_object_adapter():
    """Test the object adapter pattern."""
    print("Testing Object Adapter Pattern:")
    
    # Create a legacy rectangle
    legacy_rect = LegacyRectangle(0, 0, 5, 10)
    print(f"  Legacy rectangle coordinates: {legacy_rect.get_coordinates()}")
    
    # Create an adapter
    adapted_rect = RectangleAdapter(legacy_rect)
    
    # Use the adapter through the Shape interface
    print(f"  Area: {adapted_rect.area()}")
    print(f"  Perimeter: {adapted_rect.perimeter()}")
    print(f"  Description: {adapted_rect.describe()}")

def test_class_adapter():
    """Test the class adapter pattern."""
    print("\nTesting Class Adapter Pattern:")
    
    # Create an adapter using inheritance
    adapted_rect = RectangleClassAdapter(0, 0, 5, 10)
    
    # Use the adapter through the Shape interface
    print(f"  Area: {adapted_rect.area()}")
    print(f"  Perimeter: {adapted_rect.perimeter()}")
    print(f"  Description: {adapted_rect.describe()}")
    
    # Can also use the legacy interface
    print(f"  Legacy coordinates: {adapted_rect.get_coordinates()}")

def test_function_adapter():
    """Test the function-based adapter."""
    print("\nTesting Function-based Adapter:")
    
    # Create a legacy rectangle
    legacy_rect = LegacyRectangle(0, 0, 5, 10)
    
    # Create a circle
    circle = Circle(0, 0, 5)
    
    # Use the adapter function
    shapes = [
        shape_adapter(legacy_rect),
        shape_adapter(circle)
    ]
    
    # Use the adapted objects
    for i, shape in enumerate(shapes):
        print(f"  Shape {i+1}:")
        print(f"    Area: {shape.area()}")
        print(f"    Perimeter: {shape.perimeter()}")
        print(f"    Description: {shape.describe()}")
    
    # Try with incompatible object
    try:
        shape_adapter("not a shape")
    except TypeError as e:
        print(f"  Error (expected): {e}")

def test_duck_typing_adapter():
    """Test the duck typing adapter."""
    print("\nTesting Duck Typing Adapter:")
    
    # Create a legacy rectangle
    legacy_rect = LegacyRectangle(0, 0, 5, 10)
    
    # Create a duck typing adapter
    duck_rect = DuckTypingRectangle(legacy_rect)
    
    # Use the adapter
    print(f"  Area: {duck_rect.area()}")
    print(f"  Perimeter: {duck_rect.perimeter()}")
    print(f"  Description: {duck_rect.describe()}")
    
    # Demonstrate Python's duck typing
    def print_shape_info(shape):
        print(f"    Area: {shape.area()}")
        print(f"    Perimeter: {shape.perimeter()}")
        print(f"    Description: {shape.describe()}")
    
    print("\n  Using duck typing with different shapes:")
    
    print("    Circle:")
    print_shape_info(Circle(0, 0, 5))
    
    print("    Duck typing rectangle:")
    print_shape_info(duck_rect)

if __name__ == "__main__":
    # Test each adapter implementation
    test_object_adapter()
    test_class_adapter()
    test_function_adapter()
    test_duck_typing_adapter()
    
    # Compare approaches
    print("\nAdapter Implementation Comparison:")
    print("  1. Object Adapter: Uses composition, more flexible")
    print("  2. Class Adapter: Uses inheritance, can access protected members")
    print("  3. Function Adapter: More dynamic, handles multiple types")
    print("  4. Duck Typing: Most Pythonic, focuses on behavior not hierarchy")
    
    print("\nDiscussion:")
    print("  Which adapter approach is most appropriate for Python?")
    print("  How does each approach handle changes in the adaptee interface?")
    print("  What are the trade-offs between inheritance and composition?")
