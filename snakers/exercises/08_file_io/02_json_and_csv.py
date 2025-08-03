"""
Exercise 8.2: Working with JSON and CSV Files

Learn about handling structured data files in Python.

Tasks:
1. Complete the functions below
2. Practice reading and writing JSON and CSV files
3. Learn about data serialization and parsing

Topics covered:
- JSON serialization and deserialization
- CSV reading and writing
- Working with tabular data
- Converting between different data formats
"""

from typing import List, Dict, Any, Optional
import json
import csv

def read_json_file(filename: str) -> Dict[str, Any]:
    """
    Read and parse a JSON file.
    
    Args:
        filename: Path to the JSON file
        
    Returns:
        Parsed JSON data as dictionary
    """
    # TODO: Open file and use json.load() to parse it
    pass

def write_json_file(filename: str, data: Dict[str, Any], indent: int = 4) -> None:
    """
    Write data to a JSON file.
    
    Args:
        filename: Path to the JSON file
        data: Dictionary to serialize
        indent: Indentation level (default: 4)
    """
    # TODO: Open file for writing and use json.dump() to write data
    # TODO: Use indent parameter for pretty printing
    pass

def read_csv_file(filename: str, has_header: bool = True) -> List[Dict[str, str]]:
    """
    Read a CSV file into a list of dictionaries.
    
    Args:
        filename: Path to the CSV file
        has_header: Whether the CSV has a header row
        
    Returns:
        List of dictionaries, each representing a row
    """
    # TODO: Open CSV file and read it using csv.reader or csv.DictReader
    # TODO: If has_header is True, use DictReader
    # TODO: Otherwise, create dictionaries with column indices as keys
    pass

def write_csv_file(filename: str, data: List[Dict[str, Any]], fieldnames: Optional[List[str]] = None) -> None:
    """
    Write a list of dictionaries to a CSV file.
    
    Args:
        filename: Path to the CSV file
        data: List of dictionaries to write
        fieldnames: List of field names (if None, use keys from first dictionary)
    """
    # TODO: If fieldnames is None, extract them from the first dictionary
    # TODO: Open file and use csv.DictWriter to write data
    # TODO: Write header and then rows
    pass

def convert_csv_to_json(csv_file: str, json_file: str) -> None:
    """
    Convert a CSV file to JSON format.
    
    Args:
        csv_file: Path to the input CSV file
        json_file: Path to the output JSON file
    """
    # TODO: Read CSV file
    # TODO: Write data to JSON file
    pass

def convert_json_to_csv(json_file: str, csv_file: str) -> None:
    """
    Convert a JSON file to CSV format.
    
    Args:
        json_file: Path to the input JSON file
        csv_file: Path to the output CSV file
    """
    # TODO: Read JSON file
    # TODO: If JSON contains a list of dictionaries, write directly to CSV
    # TODO: If JSON structure is more complex, flatten it appropriately
    pass

def find_in_json(json_file: str, key: str) -> List[Any]:
    """
    Find all values for a given key in a JSON file (at any nesting level).
    
    Args:
        json_file: Path to the JSON file
        key: Key to search for
        
    Returns:
        List of values found for the key
    """
    # TODO: Read JSON file
    # TODO: Implement a recursive function to search for key at any level
    # TODO: Return all matching values
    pass

if __name__ == "__main__":
    # Sample data for testing
    sample_data = {
        "name": "John Doe",
        "age": 30,
        "skills": ["Python", "JavaScript", "SQL"],
        "contact": {
            "email": "john@example.com",
            "phone": "123-456-7890"
        }
    }
    
    # Test JSON functions
    write_json_file("sample.json", sample_data)
    loaded_data = read_json_file("sample.json")
    print("Loaded JSON data:", loaded_data)
    
    # Sample CSV data
    csv_data = [
        {"name": "Alice", "age": "25", "city": "New York"},
        {"name": "Bob", "age": "30", "city": "Boston"},
        {"name": "Charlie", "age": "35", "city": "Chicago"}
    ]
    
    # Test CSV functions
    write_csv_file("sample.csv", csv_data)
    loaded_csv = read_csv_file("sample.csv")
    print("Loaded CSV data:", loaded_csv)
    
    # Test conversion functions
    convert_csv_to_json("sample.csv", "csv_to_json.json")
    convert_json_to_csv("csv_to_json.json", "json_to_csv.csv")
    
    # Test find in JSON
    emails = find_in_json("sample.json", "email")
    print("Found emails:", emails)
