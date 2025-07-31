"""
Exercise 2.2: Dictionary Operations

Learn about Python dictionaries and key-value operations.

Tasks:
1. Complete the functions below
2. Practice dictionary creation and manipulation
3. Learn about dictionary methods and iteration

Topics covered:
- Dictionary creation and access
- Dictionary methods (keys, values, items)
- Dictionary comprehensions
- Counting and grouping with dictionaries
"""

from typing import Dict, List

def create_student_grades() -> Dict[str, int]:
    """
    Create a dictionary of student names and their grades.
    
    Returns:
        Dictionary with student names as keys and grades as values
        
    Example:
        {"Alice": 85, "Bob": 92, "Charlie": 78}
    """
    # TODO: Create a dictionary with at least 3 students and their grades
    pass

def get_student_grade(grades: Dict[str, int], student_name: str) -> int:
    """
    Get a student's grade, return -1 if not found.
    
    Args:
        grades: Dictionary of student grades
        student_name: Name of the student
        
    Returns:
        Student's grade or -1 if not found
    """
    # TODO: Use .get() method to safely get the grade
    # TODO: Return -1 if student not found
    pass

def count_word_frequency(text: str) -> Dict[str, int]:
    """
    Count how many times each word appears in text.
    
    Args:
        text: Input text
        
    Returns:
        Dictionary with words as keys and counts as values
        
    Example:
        >>> count_word_frequency("hello world hello")
        {"hello": 2, "world": 1}
    """
    # TODO: Split text into words
    # TODO: Count each word using a dictionary
    pass

def find_top_student(grades: Dict[str, int]) -> str:
    """
    Find the student with the highest grade.
    
    Args:
        grades: Dictionary of student grades
        
    Returns:
        Name of student with highest grade
    """
    # TODO: Use max() with key parameter
    # TODO: grades.get as the key function
    pass

def group_by_grade_level(grades: Dict[str, int]) -> Dict[str, List[str]]:
    """
    Group students by grade level (A: 90+, B: 80-89, C: 70-79, F: below 70).
    
    Args:
        grades: Dictionary of student grades
        
    Returns:
        Dictionary with grade levels as keys and student lists as values
    """
    # TODO: Create result dictionary with empty lists for each grade
    # TODO: Iterate through grades and categorize each student
    pass

def merge_class_grades(class1: Dict[str, int], class2: Dict[str, int]) -> Dict[str, int]:
    """
    Merge grades from two classes.
    
    Args:
        class1: First class grades
        class2: Second class grades
        
    Returns:
        Combined grades dictionary
    """
    # TODO: Create new dictionary with both classes
    # TODO: Handle duplicate student names (keep higher grade)
    pass

if __name__ == "__main__":
    # Test your functions
    grades = create_student_grades()
    print("Student grades:", grades)
    
    # Test getting a grade
    alice_grade = get_student_grade(grades, "Alice")
    unknown_grade = get_student_grade(grades, "Unknown")
    print(f"Alice's grade: {alice_grade}, Unknown grade: {unknown_grade}")
    
    # Test word frequency
    text = "python is great python is fun python programming"
    frequency = count_word_frequency(text)
    print("Word frequency:", frequency)
    
    # Test top student
    top_student = find_top_student(grades)
    print("Top student:", top_student)
    
    # Test grouping
    grouped = group_by_grade_level(grades)
    print("Grouped by grade level:", grouped)
    
    # Test merging
    class2_grades = {"David": 88, "Eve": 95, "Alice": 90}  # Alice appears in both
    merged = merge_class_grades(grades, class2_grades)
    print("Merged grades:", merged)
    # Test nested operations
    nested_data = {
        "user": {
            "profile": {
                "name": "John",
                "settings": {"theme": "dark"}
            }
        }
    }
    
    name = nested_get(nested_data, "user.profile.name")
    theme = nested_get(nested_data, "user.profile.settings.theme")
    missing = nested_get(nested_data, "user.profile.age", "unknown")
    
    print(f"Name: {name}, Theme: {theme}, Age: {missing}")
    
    flattened = flatten_dictionary(nested_data)
    print("Flattened:", flattened)
