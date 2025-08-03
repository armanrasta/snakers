"""
Exercise 6.1: Basic Classes

Learn about Python classes, attributes, and methods.

Tasks:
1. Complete the class implementations below
2. Practice with class attributes and instance methods
3. Learn about object-oriented programming concepts

Topics covered:
- Class definition with attributes
- Instance methods
- Constructor (__init__)
- Special methods (__str__, __repr__)
- Object instances and interactions
"""

from typing import List, Optional

class Rectangle:
    """
    A simple Rectangle class with width and height.
    """
    
    def __init__(self, width: float, height: float):
        """
        Initialize Rectangle with width and height.
        
        Args:
            width: Width of rectangle
            height: Height of rectangle
        """
        # TODO: Initialize width and height attributes
        pass
    
    def area(self) -> float:
        """
        Calculate the area of the rectangle.
        
        Returns:
            Area (width * height)
        """
        # TODO: Calculate and return area
        pass
    
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.
        
        Returns:
            Perimeter (2 * (width + height))
        """
        # TODO: Calculate and return perimeter
        pass
    
    def is_square(self) -> bool:
        """
        Check if the rectangle is a square.
        
        Returns:
            True if width equals height, False otherwise
        """
        # TODO: Check if width equals height
        pass
    
    def __str__(self) -> str:
        """
        Return string representation of the rectangle.
        
        Returns:
            String in format "Rectangle(width=X, height=Y)"
        """
        # TODO: Return formatted string
        pass

class BankAccount:
    """
    A simple bank account class.
    """
    
    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0):
        """
        Initialize bank account.
        
        Args:
            account_number: Account number
            owner_name: Name of account owner
            balance: Initial balance (default 0.0)
        """
        # TODO: Initialize attributes
        pass
    
    def deposit(self, amount: float) -> float:
        """
        Deposit money into account.
        
        Args:
            amount: Amount to deposit (must be positive)
            
        Returns:
            New balance
            
        Raises:
            ValueError: If amount is negative
        """
        # TODO: Validate amount is positive
        # TODO: Add to balance and return new balance
        pass
    
    def withdraw(self, amount: float) -> float:
        """
        Withdraw money from account.
        
        Args:
            amount: Amount to withdraw (must be positive)
            
        Returns:
            New balance
            
        Raises:
            ValueError: If amount is negative or exceeds balance
        """
        # TODO: Validate amount is positive and not more than balance
        # TODO: Subtract from balance and return new balance
        pass
    
    def get_balance(self) -> float:
        """
        Get current balance.
        
        Returns:
            Current balance
        """
        # TODO: Return balance
        pass
    
    def __str__(self) -> str:
        """
        Return string representation of account.
        
        Returns:
            String with account details
        """
        # TODO: Return formatted string with account info
        pass

class Student:
    """
    A student class to track courses and grades.
    """
    
    def __init__(self, name: str, student_id: str):
        """
        Initialize student.
        
        Args:
            name: Student name
            student_id: Student ID
        """
        # TODO: Initialize attributes
        # TODO: Initialize empty grades dictionary
        pass
    
    def add_grade(self, course: str, grade: float) -> None:
        """
        Add grade for a course.
        
        Args:
            course: Course name
            grade: Course grade (0-100)
            
        Raises:
            ValueError: If grade is not between 0 and 100
        """
        # TODO: Validate grade is between 0 and 100
        # TODO: Add to grades dictionary
        pass
    
    def get_grade(self, course: str) -> Optional[float]:
        """
        Get grade for a specific course.
        
        Args:
            course: Course name
            
        Returns:
            Grade for course or None if course not found
        """
        # TODO: Return grade for course or None if not found
        pass
    
    def get_gpa(self) -> float:
        """
        Calculate grade point average.
        
        Returns:
            Average of all grades or 0.0 if no grades
        """
        # TODO: Calculate average of all grades
        # TODO: Handle case where no grades exist
        pass
    
    def __str__(self) -> str:
        """
        Return string representation of student.
        
        Returns:
            String with student information
        """
        # TODO: Return formatted string with student info
        pass

if __name__ == "__main__":
    # Test Rectangle class
    rect = Rectangle(5, 10)
    print(f"Rectangle area: {rect.area()}")
    print(f"Rectangle perimeter: {rect.perimeter()}")
    print(f"Is square? {rect.is_square()}")
    print(rect)
    
    square = Rectangle(5, 5)
    print(f"Square area: {square.area()}")
    print(f"Is square? {square.is_square()}")
    
    # Test BankAccount class
    account = BankAccount("12345", "John Doe", 100.0)
    print(account)
    
    account.deposit(50.0)
    print(f"After deposit: {account.get_balance()}")
    
    account.withdraw(25.0)
    print(f"After withdrawal: {account.get_balance()}")
    
    # Test Student class
    student = Student("Alice Smith", "S12345")
    student.add_grade("Math", 85)
    student.add_grade("Science", 92)
    student.add_grade("History", 78)
    
    print(student)
    print(f"Math grade: {student.get_grade('Math')}")
    print(f"GPA: {student.get_gpa()}")
