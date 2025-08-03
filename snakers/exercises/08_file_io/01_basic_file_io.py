"""
Exercise 8.1: Basic File I/O

Learn about Python's file handling capabilities.

Tasks:
1. Complete the functions below
2. Practice reading from and writing to files
3. Learn about different file modes and context managers

Topics covered:
- File opening and closing
- Reading file content
- Writing to files
- Context managers (with statement)
- File modes (r, w, a, b)
"""

from typing import List, Dict, Any, Optional
import os

def read_file_content(filename: str) -> str:
    """
    Read and return the entire content of a file.
    
    Args:
        filename: Path to the file
        
    Returns:
        File content as a string
        
    Example:
        >>> read_file_content("sample.txt")
        "Hello, world!"
    """
    # TODO: Open the file in read mode
    # TODO: Use with statement (context manager)
    # TODO: Read the entire content and return it
    pass

def write_to_file(filename: str, content: str, append: bool = False) -> None:
    """
    Write content to a file.
    
    Args:
        filename: Path to the file
        content: Content to write
        append: If True, append to existing content; if False, overwrite
    """
    # TODO: Open file in write ('w') or append ('a') mode based on append parameter
    # TODO: Use with statement
    # TODO: Write content to file
    pass

def read_lines(filename: str) -> List[str]:
    """
    Read a file and return a list of lines with newlines removed.
    
    Args:
        filename: Path to the file
        
    Returns:
        List of lines from the file
        
    Example:
        >>> read_lines("sample.txt")
        ["Line 1", "Line 2", "Line 3"]
    """
    # TODO: Open file in read mode
    # TODO: Read lines into a list
    # TODO: Strip newline characters from each line
    pass

def count_words_in_file(filename: str) -> Dict[str, int]:
    """
    Count the frequency of each word in a file.
    
    Args:
        filename: Path to the file
        
    Returns:
        Dictionary mapping words to their frequencies
        
    Example:
        >>> count_words_in_file("sample.txt")
        {"hello": 2, "world": 1}
    """
    # TODO: Read file content
    # TODO: Split content into words (consider lowercase and removing punctuation)
    # TODO: Count word frequencies and return as dictionary
    pass

def check_file_exists(filename: str) -> bool:
    """
    Check if a file exists.
    
    Args:
        filename: Path to the file
        
    Returns:
        True if file exists, False otherwise
    """
    # TODO: Use os.path.exists() to check if file exists
    pass

def copy_file(source: str, destination: str) -> bool:
    """
    Copy a file from source to destination.
    
    Args:
        source: Source file path
        destination: Destination file path
        
    Returns:
        True if successful, False otherwise
    """
    # TODO: Check if source file exists
    # TODO: Read content from source
    # TODO: Write content to destination
    # TODO: Return True if successful, False otherwise
    pass

if __name__ == "__main__":
    # Create sample files for testing
    sample_text = "Hello, world!\nThis is a sample file.\nPython file I/O is fun!"
    write_to_file("sample.txt", sample_text)
    
    # Test reading functions
    content = read_file_content("sample.txt")
    print(f"File content:\n{content}")
    
    lines = read_lines("sample.txt")
    print(f"Lines: {lines}")
    
    word_count = count_words_in_file("sample.txt")
    print(f"Word frequencies: {word_count}")
    
    # Test file operations
    exists = check_file_exists("sample.txt")
    print(f"File exists: {exists}")
    
    success = copy_file("sample.txt", "sample_copy.txt")
    print(f"Copy successful: {success}")
    
    # Append to file
    write_to_file("sample.txt", "\nThis line was appended!", append=True)
    new_content = read_file_content("sample.txt")
    print(f"Updated content:\n{new_content}")
