"""
Exercise 1: Variables and Basic Types

Learn about Python variables, type hints, and basic operations.

Tasks:
1. Create variables with proper type hints
2. Fix the function to return the correct result
3. Make sure all code follows Python best practices

Hints:
- Use type hints for better code clarity
- Variables should have descriptive names
- Follow PEP 8 naming conventions
"""

# TODO: Create a variable 'name' with your name as a string
# TODO: Create a variable 'age' with your age as an integer
# TODO: Create a variable 'height' with your height in meters as a float

def calculate_bmi(weight: float, height: float) -> float:
    """Calculate Body Mass Index"""
    # TODO: Implement BMI calculation (weight / height^2)
    pass

def greet_person(name: str, age: int) -> str:
    """Create a greeting message"""
    # TODO: Return a greeting message like "Hello, Alice! You are 25 years old."
    pass

if __name__ == "__main__":
    # TODO: Remove this line when you've implemented the variables above
    name, age, height = "TODO", 0, 0.0
    
    print(greet_person(name, age))
    
    # Example usage (uncomment when ready)
    # weight = 70.0  # kg
    # bmi = calculate_bmi(weight, height)
    # print(f"Your BMI is: {bmi:.1f}")
