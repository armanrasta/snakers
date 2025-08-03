"""
Exercise 16.2: Package Management

Learn how to manage Python packages using different tools.

Tasks:
1. Complete the functions for package management
2. Learn about pip, poetry, and pipenv
3. Practice installing, updating, and managing dependencies

Topics covered:
- Using pip for package management
- Working with poetry
- Managing dependencies with pipenv
- Handling version constraints
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

def install_package(package_name: str, version: Optional[str] = None) -> Tuple[bool, str]:
    """
    Install a Python package using pip.
    
    Args:
        package_name: Name of the package
        version: Optional version specification
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Construct pip install command with package name and version if specified
    # TODO: Execute the command using subprocess
    # TODO: Return success/failure and message
    pass

def uninstall_package(package_name: str) -> Tuple[bool, str]:
    """
    Uninstall a Python package using pip.
    
    Args:
        package_name: Name of the package
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Construct pip uninstall command
    # TODO: Execute the command using subprocess with -y flag
    # TODO: Return success/failure and message
    pass

def get_package_info(package_name: str) -> Dict[str, Any]:
    """
    Get information about an installed package.
    
    Args:
        package_name: Name of the package
        
    Returns:
        Dictionary with package information
    """
    # TODO: Use pip show command to get package info
    # TODO: Parse the output into a dictionary
    # TODO: Return the information dictionary
    pass

def update_package(package_name: str) -> Tuple[bool, str]:
    """
    Update a package to the latest version.
    
    Args:
        package_name: Name of the package
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Use pip install --upgrade command
    # TODO: Return success/failure and message
    pass

def parse_requirements(requirements_file: str) -> List[Dict[str, str]]:
    """
    Parse a requirements.txt file into structured data.
    
    Args:
        requirements_file: Path to requirements.txt
        
    Returns:
        List of dictionaries with package info
    """
    # TODO: Read the requirements file
    # TODO: Parse each line into a dictionary with name, version, etc.
    # TODO: Return the structured data
    pass

def create_poetry_project(project_name: str, directory: Optional[Path] = None) -> Tuple[bool, str]:
    """
    Create a new Poetry project.
    
    Args:
        project_name: Name of the project
        directory: Optional directory path
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Check if poetry is installed
    # TODO: Run poetry new command
    # TODO: Return success/failure and message
    pass

def add_dependency_to_poetry(project_dir: Path, package_name: str, dev: bool = False) -> Tuple[bool, str]:
    """
    Add a dependency to a Poetry project.
    
    Args:
        project_dir: Path to the Poetry project
        package_name: Name of the package to add
        dev: Whether it's a development dependency
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Change to the project directory
    # TODO: Run poetry add command with --dev flag if needed
    # TODO: Return success/failure and message
    pass

def initialize_pipenv(directory: Optional[Path] = None) -> Tuple[bool, str]:
    """
    Initialize a pipenv environment.
    
    Args:
        directory: Optional directory path
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Check if pipenv is installed
    # TODO: Run pipenv --python command to initialize
    # TODO: Return success/failure and message
    pass

def compare_dependency_tools() -> Dict[str, List[str]]:
    """
    Compare different dependency management tools.
    
    Returns:
        Dictionary with pros and cons of each tool
    """
    # TODO: Return dictionary with pip, poetry, and pipenv pros and cons
    pass

class PackageManager:
    """A class to manage Python packages."""
    
    def __init__(self, tool: str = "pip"):
        """
        Initialize the package manager.
        
        Args:
            tool: The package management tool to use ('pip', 'poetry', 'pipenv')
        """
        self.tool = tool
        # TODO: Check if the selected tool is installed
        
    def install(self, package_name: str, version: Optional[str] = None) -> Tuple[bool, str]:
        """
        Install a package using the selected tool.
        
        Args:
            package_name: Name of the package
            version: Optional version specification
            
        Returns:
            Tuple of (success, message)
        """
        # TODO: Implement installation logic for each tool
        pass
    
    def uninstall(self, package_name: str) -> Tuple[bool, str]:
        """
        Uninstall a package using the selected tool.
        
        Args:
            package_name: Name of the package
            
        Returns:
            Tuple of (success, message)
        """
        # TODO: Implement uninstallation logic for each tool
        pass
    
    def list_packages(self) -> List[Dict[str, str]]:
        """
        List installed packages using the selected tool.
        
        Returns:
            List of dictionaries with package information
        """
        # TODO: Implement listing logic for each tool
        pass

if __name__ == "__main__":
    # Example usage
    print("Package Management Tool")
    print("----------------------")
    
    # Install a package if requested
    if len(sys.argv) > 1 and sys.argv[1] == "install":
        package = sys.argv[2] if len(sys.argv) > 2 else "requests"
        version = sys.argv[3] if len(sys.argv) > 3 else None
        success, message = install_package(package, version)
        print(message)
    
    # Show package info if requested
    if len(sys.argv) > 1 and sys.argv[1] == "info":
        package = sys.argv[2] if len(sys.argv) > 2 else "requests"
        info = get_package_info(package)
        print(f"\nPackage information for {package}:")
        for key, value in info.items():
            print(f"  {key}: {value}")
    
    # Compare tools if requested
    if len(sys.argv) > 1 and sys.argv[1] == "compare":
        comparison = compare_dependency_tools()
        print("\nComparison of package management tools:")
        for tool, points in comparison.items():
            print(f"\n{tool}:")
            for point in points:
                print(f"  - {point}")
