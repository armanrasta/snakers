"""
Exercise 4.1: Conditionals

Learn about Python's conditional statements and Boolean logic.

Tasks:
1. Complete the functions below
2. Practice with if, elif, and else statements
3. Learn about Boolean operations and comparisons

Topics covered:
- if/elif/else statements
- Boolean operators (and, or, not)
- Comparison operators (==, !=, >, <, >=, <=)
- Conditional expressions (ternary operator)
"""

def check_number_status(number: int) -> str:
    """
    Check if a number is positive, negative, or zero.
    
    Args:
        number: Input number
        
    Returns:
        "Positive" if > 0, "Negative" if < 0, "Zero" if == 0
        
    Example:
        >>> check_number_status(5)
        "Positive"
    """
    # TODO: Use if/elif/else to check number status
    pass

def determine_grade(score: float) -> str:
    """
    Determine the letter grade based on a score.
    
    Args:
        score: Numeric score (0-100)
        
    Returns:
        Letter grade (A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60)
        
    Example:
        >>> determine_grade(85)
        "B"
    """
    # TODO: Use if/elif/else to determine grade
    pass

def is_leap_year(year: int) -> bool:
    """
    Check if a year is a leap year.
    
    Args:
        year: Year to check
        
    Returns:
        True if leap year, False otherwise
        
    Rules:
        - Years divisible by 4 are leap years
        - Except years divisible by 100 are not leap years
        - Unless they are also divisible by 400, then they are leap years
        
    Example:
        >>> is_leap_year(2020)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2000)
        True
    """
    # TODO: Implement leap year logic
    pass

def calculate_shipping(subtotal: float, express: bool = False) -> float:
    """
    Calculate shipping cost based on order subtotal and shipping method.
    
    Args:
        subtotal: Order subtotal
        express: Whether express shipping is selected (default: False)
        
    Returns:
        Shipping cost
        
    Rules:
        - Free standard shipping for orders over $50
        - $5.99 standard shipping for orders under $50
        - Express shipping adds $10 to standard shipping cost
        
    Example:
        >>> calculate_shipping(45.99)
        5.99
        >>> calculate_shipping(45.99, express=True)
        15.99
    """
    # TODO: Calculate shipping based on conditions
    pass

def max_of_three(a: int, b: int, c: int) -> int:
    """
    Find the maximum of three numbers.
    
    Args:
        a: First number
        b: Second number
        c: Third number
        
    Returns:
        Maximum value
        
    Example:
        >>> max_of_three(5, 12, 9)
        12
    """
    # TODO: Find maximum using if/elif/else statements
    pass

def check_access(age: int, is_admin: bool) -> str:
    """
    Check if user has access based on age and admin status.
    
    Args:
        age: User's age
        is_admin: Whether user is an admin
        
    Returns:
        Access status message
        
    Rules:
        - Admins always have "Full access"
        - Users 18+ have "Standard access"
        - Users under 18 have "Restricted access"
        
    Example:
        >>> check_access(15, False)
        "Restricted access"
    """
    # TODO: Use Boolean logic to determine access
    pass

if __name__ == "__main__":
    # Test your functions
    print(f"Status of 5: {check_number_status(5)}")
    print(f"Status of 0: {check_number_status(0)}")
    print(f"Status of -10: {check_number_status(-10)}")
    
    print(f"Grade for 95: {determine_grade(95)}")
    print(f"Grade for 85: {determine_grade(85)}")
    print(f"Grade for 75: {determine_grade(75)}")
    print(f"Grade for 65: {determine_grade(65)}")
    print(f"Grade for 55: {determine_grade(55)}")
    
    years = [2020, 1900, 2000, 2023]
    for year in years:
        print(f"{year} is leap year: {is_leap_year(year)}")
    
    print(f"Shipping for $45.99: ${calculate_shipping(45.99)}")
    print(f"Shipping for $45.99 (express): ${calculate_shipping(45.99, True)}")
    print(f"Shipping for $60.00: ${calculate_shipping(60.00)}")
    
    print(f"Max of 5, 12, 9: {max_of_three(5, 12, 9)}")
    
    print(f"Access for 15-year-old user: {check_access(15, False)}")
    print(f"Access for 20-year-old user: {check_access(20, False)}")
    print(f"Access for 15-year-old admin: {check_access(15, True)}")
