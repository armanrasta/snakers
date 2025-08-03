"""
Exercise 0.2: Environment Check

Learn about your Python environment and system information.

Tasks:
1. Complete the functions below
2. Explore Python's system and version information
3. Learn how to access environment details

Topics covered:
- sys module
- platform information
- Python version
- Environment variables
"""

import sys
import platform
import os

def get_python_version() -> str:
    """
    Get the current Python version.
    
    Returns:
        A string with Python version information
    """
    # TODO: Return a formatted string with Python version (use sys.version_info)
    pass

def get_platform_info() -> dict:
    """
    Get information about the current platform/operating system.
    
    Returns:
        Dictionary with platform information
    """
    # TODO: Create a dictionary with platform name, version, and architecture
    # TODO: Use platform module functions like platform.system(), platform.version(), etc.
    pass

def get_path_info() -> list:
    """
    Get Python's module search path.
    
    Returns:
        List of directories in Python's module search path
    """
    # TODO: Return the module search path from sys.path
    pass

def check_installed_modules() -> list:
    """
    List some important installed modules.
    
    Returns:
        List of tuples with module name and status ('installed' or 'missing')
    """
    # TODO: Check if the following modules are installed: numpy, pandas, matplotlib, requests
    # TODO: Use try/except with import statements to check
    # TODO: Return list of (module_name, status) tuples
    pass

if __name__ == "__main__":
    print(f"Python Version: {get_python_version()}")
    
    platform_info = get_platform_info()
    print("\nPlatform Information:")
    for key, value in platform_info.items():
        print(f"  {key}: {value}")
    
    print("\nModule Search Path:")
    for i, path in enumerate(get_path_info(), 1):
        print(f"  {i}. {path}")
    
    modules = check_installed_modules()
    print("\nImportant Modules:")
    for module, status in modules:
        status_color = "✅" if status == "installed" else "❌"
        print(f"  {status_color} {module}: {status}")
