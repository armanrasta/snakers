"""
Exercise 13.1: Basic Data Processing

Learn about Python's data processing capabilities.

Tasks:
1. Complete the functions for processing data
2. Work with CSV data and transformations
3. Calculate statistics and aggregations

Topics covered:
- Reading and parsing data
- Filtering and transformations
- Aggregation and statistics
- Data export
"""

from typing import List, Dict, Any, Tuple, Optional
import csv
import statistics
from pathlib import Path

# Sample data representing student records: (name, age, grade, course)
SampleData = [
    ("Alice", 20, 85, "Math"),
    ("Bob", 22, 92, "Physics"),
    ("Charlie", 21, 78, "Math"),
    ("Diana", 23, 95, "Chemistry"),
    ("Eve", 19, 88, "Physics"),
    ("Frank", 20, 72, "Math"),
    ("Grace", 22, 90, "Chemistry"),
    ("Heidi", 21, 85, "Physics"),
]

def create_sample_csv(filename: str) -> None:
    """
    Create a sample CSV file with student data.
    
    Args:
        filename: Path to the output CSV file
    """
    # TODO: Write SampleData to a CSV file with appropriate headers
    pass

def read_student_data(filename: str) -> List[Dict[str, Any]]:
    """
    Read student data from a CSV file.
    
    Args:
        filename: Path to the CSV file
        
    Returns:
        List of dictionaries with student data
    """
    # TODO: Read the CSV file and return a list of dictionaries
    # TODO: Convert numeric fields to the appropriate types
    pass

def filter_by_course(students: List[Dict[str, Any]], course: str) -> List[Dict[str, Any]]:
    """
    Filter students by course.
    
    Args:
        students: List of student dictionaries
        course: Course name to filter by
        
    Returns:
        Filtered list of student dictionaries
    """
    # TODO: Return only students in the specified course
    pass

def calculate_statistics(students: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate statistics from student data.
    
    Args:
        students: List of student dictionaries
        
    Returns:
        Dictionary with various statistics
    """
    # TODO: Calculate average age, grade, min/max values
    # TODO: Return dictionary with all statistics
    pass

def get_top_students(students: List[Dict[str, Any]], n: int = 3) -> List[Dict[str, Any]]:
    """
    Get the top N students by grade.
    
    Args:
        students: List of student dictionaries
        n: Number of top students to return
        
    Returns:
        List of the top N student dictionaries
    """
    # TODO: Sort students by grade in descending order
    # TODO: Return the top N students
    pass

def group_by_course(students: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Group students by course.
    
    Args:
        students: List of student dictionaries
        
    Returns:
        Dictionary mapping course names to lists of student dictionaries
    """
    # TODO: Create a dictionary grouping students by course
    pass

def add_pass_fail(students: List[Dict[str, Any]], passing_grade: int = 80) -> List[Dict[str, Any]]:
    """
    Add a 'passed' field to each student record.
    
    Args:
        students: List of student dictionaries
        passing_grade: Minimum grade to pass
        
    Returns:
        Student list with added 'passed' field
    """
    # TODO: Add a boolean 'passed' field based on the grade
    # TODO: Return the modified student list
    pass

def write_report(students: List[Dict[str, Any]], filename: str) -> None:
    """
    Write a formatted report of student data.
    
    Args:
        students: List of student dictionaries
        filename: Output file path
    """
    # TODO: Write a formatted text report with student data
    # TODO: Include statistics at the end of the report
    pass

if __name__ == "__main__":
    # Create sample data file
    csv_file = "students.csv"
    create_sample_csv(csv_file)
    
    # Read and process data
    students = read_student_data(csv_file)
    print(f"Loaded {len(students)} student records")
    
    # Filter by course
    math_students = filter_by_course(students, "Math")
    print(f"Math students: {len(math_students)}")
    
    # Calculate statistics
    stats = calculate_statistics(students)
    print("Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Get top students
    top_students = get_top_students(students)
    print("Top students:")
    for i, student in enumerate(top_students, 1):
        print(f"  {i}. {student['name']} - Grade: {student['grade']}")
    
    # Group by course
    course_groups = group_by_course(students)
    print("Students by course:")
    for course, course_students in course_groups.items():
        print(f"  {course}: {len(course_students)} students")
    
    # Add pass/fail status
    students_with_status = add_pass_fail(students)
    passing = sum(1 for s in students_with_status if s['passed'])
    print(f"Passing students: {passing}/{len(students)}")
    
    # Write report
    report_file = "student_report.txt"
    write_report(students, report_file)
    print(f"Report written to {report_file}")
