"""
Exercise 18.1: Regular Expressions Basics

Learn about Python's regular expression module and pattern matching.

Tasks:
1. Complete the functions below
2. Practice with different regex patterns
3. Understand regex syntax and special characters

Topics covered:
- Basic regex patterns
- Character classes
- Quantifiers
- Groups and capturing
- Common regex functions
"""

import re
from typing import List, Optional, Dict, Tuple, Pattern

def is_valid_email(email: str) -> bool:
    """
    Check if a string is a valid email address.
    
    Args:
        email: String to check
        
    Returns:
        True if valid email, False otherwise
        
    Example:
        >>> is_valid_email("user@example.com")
        True
        >>> is_valid_email("invalid.email")
        False
    """
    # TODO: Implement regex pattern for basic email validation
    # TODO: Use re.match to check if the pattern matches
    pass

def extract_phone_numbers(text: str) -> List[str]:
    """
    Extract all phone numbers from text.
    
    Args:
        text: Text to search
        
    Returns:
        List of phone numbers found
        
    Example:
        >>> extract_phone_numbers("Call me at 123-456-7890 or (987) 654-3210")
        ['123-456-7890', '(987) 654-3210']
    """
    # TODO: Implement regex pattern for phone numbers
    # TODO: Use re.findall to extract all matches
    pass

def replace_urls(text: str, replacement: str = "[URL]") -> str:
    """
    Replace all URLs in text with a placeholder.
    
    Args:
        text: Text to process
        replacement: Replacement string
        
    Returns:
        Text with URLs replaced
        
    Example:
        >>> replace_urls("Visit https://example.com and http://test.org")
        "Visit [URL] and [URL]"
    """
    # TODO: Implement regex pattern for URLs
    # TODO: Use re.sub to replace matches
    pass

def parse_name_parts(full_name: str) -> Dict[str, str]:
    """
    Parse a full name into its parts.
    
    Args:
        full_name: Full name string
        
    Returns:
        Dictionary with name parts
        
    Example:
        >>> parse_name_parts("John Smith")
        {'first': 'John', 'middle': '', 'last': 'Smith'}
        >>> parse_name_parts("Mary Jane Doe")
        {'first': 'Mary', 'middle': 'Jane', 'last': 'Doe'}
    """
    # TODO: Implement regex pattern with capturing groups
    # TODO: Use re.match and access groups to extract name parts
    pass

def validate_password(password: str) -> Tuple[bool, str]:
    """
    Check if a password meets security requirements.
    
    Requirements:
    - At least 8 characters
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    
    Args:
        password: Password to validate
        
    Returns:
        Tuple of (is_valid, reason)
        
    Example:
        >>> validate_password("Abc123!")
        (True, "Password is valid")
        >>> validate_password("password")
        (False, "Password must contain at least one uppercase letter, one digit, and one special character")
    """
    # TODO: Implement regex patterns for each requirement
    # TODO: Check each requirement and return appropriate result
    pass

def extract_dates(text: str) -> List[str]:
    """
    Extract all dates from text in various formats.
    
    Args:
        text: Text to search
        
    Returns:
        List of date strings found
        
    Example:
        >>> extract_dates("Meeting on 2023-05-15 and party on 12/31/2023")
        ['2023-05-15', '12/31/2023']
    """
    # TODO: Implement regex pattern for common date formats
    # TODO: Use re.findall to extract all matches
    pass

def compile_patterns() -> Dict[str, Pattern]:
    """
    Compile regex patterns for repeated use.
    
    Returns:
        Dictionary of compiled regex patterns
    """
    # TODO: Create and compile patterns for email, phone, etc.
    # TODO: Return dictionary of compiled patterns
    pass

if __name__ == "__main__":
    # Test email validation
    emails = ["user@example.com", "invalid.email", "another@test.co.uk"]
    for email in emails:
        valid = is_valid_email(email)
        print(f"'{email}' is {'valid' if valid else 'invalid'}")
    
    # Test phone number extraction
    text = "Contact us at (123) 456-7890 or 555-987-6543 for more information."
    phones = extract_phone_numbers(text)
    print(f"Extracted phone numbers: {phones}")
    
    # Test URL replacement
    url_text = "Visit our website at https://example.com or http://www.test.org."
    replaced = replace_urls(url_text)
    print(f"With URLs replaced: {replaced}")
    
    # Test name parsing
    names = ["John Smith", "Mary Jane Doe", "Robert"]
    for name in names:
        parts = parse_name_parts(name)
        print(f"'{name}' parsed as: {parts}")
    
    # Test password validation
    passwords = ["password", "Password1", "Secure123!", "short"]
    for pwd in passwords:
        valid, reason = validate_password(pwd)
        print(f"'{pwd}': {reason}")
    
    # Test date extraction
    date_text = "Report due on 2023-05-15, meeting on 12/31/2023, and followup on 01-15-2024."
    dates = extract_dates(date_text)
    print(f"Extracted dates: {dates}")
    
    # Test compiled patterns
    patterns = compile_patterns()
    print(f"Compiled {len(patterns)} patterns")
