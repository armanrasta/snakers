"""
Exercise 3.1: Basic Functions

Learn about function definitions, parameters, and return values.

Tasks:
1. Complete the functions below
2. Practice with different parameter types
3. Learn about default parameters and return values

Topics covered:
- Function definition with def
- Parameters and arguments
- Return values and type hints
- Default parameter values
"""

def greet_person(name: str) -> str:
    """
    Create a greeting message for a person.
    
    Args:
        name: Name of the person to greet
        
    Returns:
        Greeting message
        
    Example:
        >>> greet_person("Alice")
        "Hello, Alice!"
    """
    # TODO: Return a greeting message like "Hello, Alice!"
    pass

def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of the two numbers
    """
    # TODO: Return the sum of a and b
    pass

def calculate_area(length: float, width: float = 1.0) -> float:
    """
    Calculate area of a rectangle. Width defaults to 1.0 for squares.
    
    Args:
        length: Length of rectangle
        width: Width of rectangle (default: 1.0)
        
    Returns:
        Area of the rectangle
    """
    # TODO: Calculate and return length * width
    pass

def is_even(number: int) -> bool:
    """
    Check if a number is even.
    
    Args:
        number: Number to check
        
    Returns:
        True if even, False if odd
    """
    # TODO: Return True if number is even (number % 2 == 0)
    pass

def get_full_name(first_name: str, last_name: str, middle_name: str = "") -> str:
    """
    Combine names into a full name.
    
    Args:
        first_name: First name
        last_name: Last name
        middle_name: Middle name (optional)
        
    Returns:
        Full name string
        
    Example:
        >>> get_full_name("John", "Doe")
        "John Doe"
        >>> get_full_name("John", "Doe", "Smith")
        "John Smith Doe"
    """
    # TODO: Combine names appropriately
    # TODO: Handle case when middle_name is empty
    pass

def count_words(text: str) -> int:
    """
    Count the number of words in text.
    
    Args:
        text: Input text
        
    Returns:
        Number of words
    """
    # TODO: Split text and return the count
    pass

def find_maximum(numbers: list) -> int:
    """
    Find the maximum number in a list.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Maximum number
    """
    # TODO: Use max() function to find the maximum
    pass

if __name__ == "__main__":
    # Test your functions
    print(greet_person("Alice"))
    print(greet_person("Bob"))
    
    print("5 + 3 =", add_numbers(5, 3))
    
    print("Area of 5x3 rectangle:", calculate_area(5, 3))
    print("Area of 4x1 square:", calculate_area(4))  # Uses default width
    
    print("Is 4 even?", is_even(4))
    print("Is 7 even?", is_even(7))
    
    print("Full name:", get_full_name("John", "Doe"))
    print("Full name with middle:", get_full_name("John", "Doe", "Smith"))
    
    print("Word count:", count_words("Hello world from Python"))
    
    print("Maximum:", find_maximum([1, 5, 3, 9, 2]))
    print(f"Sum: {total}")
    
    # Test profile creation
    profile = create_profile(
        name="John Doe",
        email="john@example.com",
        age=30,
        city="New York"
    )
    print(f"Profile: {profile}")
    
    # Test safe division
    result1 = safe_divide(10, 2)
    result2 = safe_divide(10, 0)
    print(f"10/2 = {result1}, 10/0 = {result2}")
    
    # Test name parsing
    names = ["John Doe", "Mary Jane Smith", "Prince"]
    for name in names:
        parsed = parse_name(name)
        print(f"'{name}' -> {parsed}")
