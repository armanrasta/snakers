"""
Exercise 16.1: Virtual Environments

Learn how to create and manage Python virtual environments.

Tasks:
1. Complete the functions to manage virtual environments
2. Learn about venv and other environment management tools
3. Practice creating, activating, and managing dependencies

Topics covered:
- Creating virtual environments with venv
- Activating and deactivating environments
- Managing packages in isolated environments
- Requirements files
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Optional, Tuple

def create_virtual_environment(env_name: str, path: Optional[Path] = None) -> Tuple[bool, str]:
    """
    Create a new virtual environment.
    
    Args:
        env_name: Name of the virtual environment
        path: Path where to create the environment (default: current directory)
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Use the venv module to create a virtual environment
    # TODO: Return success status and appropriate message
    pass

def list_installed_packages(env_path: Path) -> List[str]:
    """
    List packages installed in a virtual environment.
    
    Args:
        env_path: Path to the virtual environment
        
    Returns:
        List of installed package names with versions
    """
    # TODO: Use subprocess to run pip list in the virtual environment
    # TODO: Parse and return the results
    pass

def generate_requirements_file(env_path: Path, output_file: str = "requirements.txt") -> Tuple[bool, str]:
    """
    Generate a requirements.txt file from installed packages.
    
    Args:
        env_path: Path to the virtual environment
        output_file: Name of the output file
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Use subprocess to run pip freeze and capture output
    # TODO: Write output to the requirements file
    # TODO: Return success status and message
    pass

def install_from_requirements(env_path: Path, requirements_file: str) -> Tuple[bool, str]:
    """
    Install packages from a requirements file.
    
    Args:
        env_path: Path to the virtual environment
        requirements_file: Path to the requirements file
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Use subprocess to run pip install -r with the requirements file
    # TODO: Return success status and message
    pass

def check_environment_status() -> Dict[str, any]:
    """
    Check if currently running in a virtual environment.
    
    Returns:
        Dictionary with environment information
    """
    # TODO: Detect if code is running in a virtual environment
    # TODO: Return dictionary with environment info (is_venv, path, python_version)
    pass

def compare_with_requirements(env_path: Path, requirements_file: str) -> Dict[str, List[str]]:
    """
    Compare installed packages with those in a requirements file.
    
    Args:
        env_path: Path to the virtual environment
        requirements_file: Path to the requirements file
        
    Returns:
        Dictionary with missing, outdated, and extra packages
    """
    # TODO: Parse requirements file to get expected packages
    # TODO: Get installed packages
    # TODO: Compare and return differences (missing, outdated, extra)
    pass

class VenvChecker:
    """A class to check and validate virtual environments."""
    
    def __init__(self, env_path: Optional[Path] = None):
        self.env_path = env_path or Path.cwd() / "venv"
        
    def exists(self) -> bool:
        """Check if the virtual environment exists."""
        # TODO: Check if the environment directory exists
        # TODO: Verify it has the expected structure
        pass
    
    def is_activated(self) -> bool:
        """Check if the environment is currently activated."""
        # TODO: Check if the current Python interpreter is from this environment
        pass
    
    def get_packages(self) -> List[Dict[str, str]]:
        """Get a list of installed packages with details."""
        # TODO: Get detailed information about installed packages
        pass
    
    def check_package_installed(self, package_name: str) -> bool:
        """Check if a specific package is installed."""
        # TODO: Check if the package is in the list of installed packages
        pass

if __name__ == "__main__":
    # Example usage
    print("Virtual Environment Management Tool")
    print("----------------------------------")
    
    # Check current environment status
    status = check_environment_status()
    print(f"Running in virtual environment: {status.get('is_venv', False)}")
    if status.get('is_venv'):
        print(f"Environment path: {status.get('path')}")
        print(f"Python version: {status.get('python_version')}")
    
    # Create a new environment if requested
    if len(sys.argv) > 1 and sys.argv[1] == "create":
        env_name = sys.argv[2] if len(sys.argv) > 2 else "venv"
        success, message = create_virtual_environment(env_name)
        print(message)
    
    # List packages if requested
    if len(sys.argv) > 1 and sys.argv[1] == "list":
        env_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd() / "venv"
        packages = list_installed_packages(env_path)
        print("\nInstalled packages:")
        for package in packages:
            print(f"  {package}")
    
    # Generate requirements file if requested
    if len(sys.argv) > 1 and sys.argv[1] == "freeze":
        env_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd() / "venv"
        output = sys.argv[3] if len(sys.argv) > 3 else "requirements.txt"
        success, message = generate_requirements_file(env_path, output)
        print(message)
        
    # Install from requirements file if requested
    if len(sys.argv) > 1 and sys.argv[1] == "install":
        env_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd() / "venv"
        req_file = sys.argv[3] if len(sys.argv) > 3 else "requirements.txt"
        success, message = install_from_requirements(env_path, req_file)
        print(message)
