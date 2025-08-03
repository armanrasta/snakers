"""
Exercise 15.1: Date and Time Handling

Learn about Python's datetime module for working with dates and times.

Tasks:
1. Complete the functions below
2. Practice with date, time, and datetime objects
3. Learn about time zones and formatting

Topics covered:
- Creating date and time objects
- Date arithmetic
- Formatting and parsing
- Time zones with pytz
- Time deltas
"""

from datetime import datetime, date, time, timedelta
from typing import List, Tuple, Optional, Dict
import calendar

# Optional: Try importing pytz for timezone handling
try:
    import pytz
    HAS_PYTZ = True
except ImportError:
    HAS_PYTZ = False

def get_current_datetime() -> datetime:
    """
    Get the current date and time.
    
    Returns:
        Current datetime object
    """
    # TODO: Return the current datetime
    pass

def create_specific_date(year: int, month: int, day: int) -> date:
    """
    Create a date object for a specific date.
    
    Args:
        year: Year
        month: Month
        day: Day
        
    Returns:
        Date object
    """
    # TODO: Create and return a date object
    pass

def add_days(input_date: date, days: int) -> date:
    """
    Add a number of days to a date.
    
    Args:
        input_date: Starting date
        days: Number of days to add (can be negative)
        
    Returns:
        New date after adding days
    """
    # TODO: Add days using timedelta
    pass

def days_between(date1: date, date2: date) -> int:
    """
    Calculate the number of days between two dates.
    
    Args:
        date1: First date
        date2: Second date
        
    Returns:
        Absolute number of days between dates
    """
    # TODO: Calculate days between dates
    # TODO: Return absolute value of difference
    pass

def format_date(input_date: date, format_string: str = "%Y-%m-%d") -> str:
    """
    Format a date using the specified format string.
    
    Args:
        input_date: Date to format
        format_string: Format string (default: ISO format)
        
    Returns:
        Formatted date string
    """
    # TODO: Format the date and return the string
    pass

def parse_date(date_string: str, format_string: str = "%Y-%m-%d") -> Optional[date]:
    """
    Parse a date string using the specified format.
    
    Args:
        date_string: Date string to parse
        format_string: Format string
        
    Returns:
        Date object or None if parsing fails
    """
    # TODO: Parse the date string
    # TODO: Handle ValueError and return None if parsing fails
    pass

def is_leap_year(year: int) -> bool:
    """
    Check if a year is a leap year.
    
    Args:
        year: Year to check
        
    Returns:
        True if leap year, False otherwise
    """
    # TODO: Use calendar module to check if leap year
    pass

def get_weekday_name(input_date: date) -> str:
    """
    Get the weekday name for a date.
    
    Args:
        input_date: Date to check
        
    Returns:
        Weekday name (e.g., "Monday")
    """
    # TODO: Get weekday name
    pass

def get_month_calendar(year: int, month: int) -> List[List[int]]:
    """
    Get a calendar for the specified month.
    
    Args:
        year: Year
        month: Month
        
    Returns:
        Nested list representing month calendar
    """
    # TODO: Use calendar module to get month calendar
    pass

def convert_timezone(dt: datetime, from_tz: str, to_tz: str) -> Optional[datetime]:
    """
    Convert datetime from one timezone to another.
    
    Args:
        dt: Datetime object
        from_tz: Source timezone name
        to_tz: Target timezone name
        
    Returns:
        Converted datetime or None if pytz not available
    """
    # TODO: Check if pytz is available
    # TODO: Convert timezone if possible
    # TODO: Return None if pytz not available
    pass

if __name__ == "__main__":
    # Test current datetime
    now = get_current_datetime()
    print(f"Current datetime: {now}")
    
    # Test creating specific date
    birthday = create_specific_date(1990, 5, 15)
    print(f"Birthday: {birthday}")
    
    # Test adding days
    future_date = add_days(date.today(), 10)
    past_date = add_days(date.today(), -10)
    print(f"10 days from today: {future_date}")
    print(f"10 days ago: {past_date}")
    
    # Test days between
    days = days_between(date(2023, 1, 1), date(2023, 12, 31))
    print(f"Days between Jan 1 and Dec 31, 2023: {days}")
    
    # Test formatting
    formatted = format_date(date.today(), "%A, %B %d, %Y")
    print(f"Formatted date: {formatted}")
    
    # Test parsing
    parsed = parse_date("2023-05-15")
    print(f"Parsed date: {parsed}")
    
    # Test leap year
    year = 2024
    leap = is_leap_year(year)
    print(f"Is {year} a leap year? {leap}")
    
    # Test weekday name
    weekday = get_weekday_name(date.today())
    print(f"Today is: {weekday}")
    
    # Test month calendar
    cal = get_month_calendar(2023, 5)
    print("May 2023 Calendar:")
    for week in cal:
        print(week)
    
    # Test timezone conversion if pytz available
    if HAS_PYTZ:
        now_utc = datetime.now(pytz.UTC)
        now_est = convert_timezone(now_utc, "UTC", "US/Eastern")
        print(f"UTC time: {now_utc}")
        print(f"Eastern time: {now_est}")
    else:
        print("pytz not available for timezone conversion")
