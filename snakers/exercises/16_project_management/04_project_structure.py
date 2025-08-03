"""
Exercise 16.4: Python Project Structure

Learn best practices for organizing Python projects.

Tasks:
1. Complete the functions to create and manage project structures
2. Learn about standard Python project layouts
3. Practice creating well-structured Python projects

Topics covered:
- Standard directory layouts
- Package vs module structure
- Configuration files
- Documentation structure
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

def create_basic_project(project_name: str, base_dir: Optional[Path] = None) -> Tuple[bool, str]:
    """
    Create a basic Python project structure.
    
    Args:
        project_name: Name of the project
        base_dir: Base directory (default: current directory)
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Create the project directory
    # TODO: Create basic structure (package dir, tests, README, etc.)
    # TODO: Return success/failure and message
    pass

def create_package_structure(package_name: str, project_dir: Path) -> Tuple[bool, str]:
    """
    Create a Python package structure within a project.
    
    Args:
        package_name: Name of the package
        project_dir: Project directory
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Create package directory with __init__.py
    # TODO: Create basic module files
    # TODO: Return success/failure and message
    pass

def create_setup_py(project_dir: Path, package_name: str, version: str = "0.1.0") -> Tuple[bool, str]:
    """
    Create a setup.py file for a Python package.
    
    Args:
        project_dir: Project directory
        package_name: Name of the package
        version: Package version
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Create a basic setup.py file with the package info
    # TODO: Return success/failure and message
    pass

def create_pyproject_toml(project_dir: Path, package_name: str, version: str = "0.1.0") -> Tuple[bool, str]:
    """
    Create a pyproject.toml file for a Python package.
    
    Args:
        project_dir: Project directory
        package_name: Name of the package
        version: Package version
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Create a basic pyproject.toml file with the package info
    # TODO: Return success/failure and message
    pass

def create_test_structure(project_dir: Path, package_name: str) -> Tuple[bool, str]:
    """
    Create a test directory structure for a Python package.
    
    Args:
        project_dir: Project directory
        package_name: Name of the package
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Create tests directory with __init__.py
    # TODO: Create basic test files
    # TODO: Return success/failure and message
    pass

def create_docs_structure(project_dir: Path) -> Tuple[bool, str]:
    """
    Create a documentation directory structure.
    
    Args:
        project_dir: Project directory
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Create docs directory with basic structure
    # TODO: Create index.md and other basic docs
    # TODO: Return success/failure and message
    pass

def convert_to_src_layout(project_dir: Path, package_name: str) -> Tuple[bool, str]:
    """
    Convert a project to use the src layout.
    
    Args:
        project_dir: Project directory
        package_name: Name of the package
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Create src directory
    # TODO: Move package to src directory
    # TODO: Update imports and setup files
    # TODO: Return success/failure and message
    pass

class ProjectTemplate:
    """A class to manage project templates."""
    
    def __init__(self, template_type: str = "basic"):
        """
        Initialize the project template manager.
        
        Args:
            template_type: Type of template ('basic', 'advanced', 'src-layout')
        """
        self.template_type = template_type
    
    def create_project(self, project_name: str, base_dir: Optional[Path] = None) -> Tuple[bool, str]:
        """
        Create a project from the template.
        
        Args:
            project_name: Name of the project
            base_dir: Base directory (default: current directory)
            
        Returns:
            Tuple of (success, message)
        """
        # TODO: Create project based on the template type
        # TODO: Return success/failure and message
        pass
    
    def list_files(self, project_dir: Path) -> List[str]:
        """
        List all files in the project.
        
        Args:
            project_dir: Project directory
            
        Returns:
            List of file paths
        """
        # TODO: Recursively find all files in the project
        # TODO: Return the list of file paths
        pass
    
    def add_optional_components(self, project_dir: Path, components: List[str]) -> Dict[str, bool]:
        """
        Add optional components to a project.
        
        Args:
            project_dir: Project directory
            components: List of component names ('ci', 'docker', 'docs', etc.)
            
        Returns:
            Dictionary mapping components to success status
        """
        # TODO: Add each requested component
        # TODO: Return success status for each component
        pass

if __name__ == "__main__":
    # Example usage
    print("Python Project Structure Tool")
    print("---------------------------")
    
    # Create a new project if requested
    if len(sys.argv) > 1 and sys.argv[1] == "create":
        project_name = sys.argv[2] if len(sys.argv) > 2 else "my_project"
        template_type = sys.argv[3] if len(sys.argv) > 3 else "basic"
        
        template = ProjectTemplate(template_type)
        success, message = template.create_project(project_name)
        print(message)
    
    # Add components if requested
    if len(sys.argv) > 1 and sys.argv[1] == "add":
        project_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        components = sys.argv[3].split(",") if len(sys.argv) > 3 else ["docs"]
        
        template = ProjectTemplate()
        results = template.add_optional_components(project_dir, components)
        
        print("\nComponent Installation Results:")
        for component, success in results.items():
            status = "✓" if success else "✗"
            print(f"{status} {component}")
    
    # Convert to src layout if requested
    if len(sys.argv) > 1 and sys.argv[1] == "convert":
        project_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        package_name = sys.argv[3] if len(sys.argv) > 3 else project_dir.name
        
        success, message = convert_to_src_layout(project_dir, package_name)
        print(message)
