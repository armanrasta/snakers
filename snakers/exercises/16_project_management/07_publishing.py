"""
Exercise 16.7: Publishing Python Packages

Learn how to prepare and publish a Python package to PyPI.

Tasks:
1. Complete the functions to prepare and publish packages
2. Learn about package distribution and versioning
3. Practice with PyPI publishing workflows

Topics covered:
- Package preparation
- Building source distributions and wheels
- Uploading to PyPI
- Release automation
"""

import os
import sys
import subprocess
import re
import shutil
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

def check_package_structure(package_dir: Path) -> Tuple[bool, List[str]]:
    """
    Check if a package structure is valid for publishing.
    
    Args:
        package_dir: Directory containing the package
        
    Returns:
        Tuple of (is_valid, issues)
    """
    # TODO: Check for required files (setup.py or pyproject.toml)
    # TODO: Check package structure
    # TODO: Return validity and list of issues
    pass

def bump_version(version_file: Path, bump_type: str = "patch") -> Tuple[bool, str]:
    """
    Bump the version number in a file.
    
    Args:
        version_file: File containing the version
        bump_type: Type of version bump ('major', 'minor', 'patch')
        
    Returns:
        Tuple of (success, new_version)
    """
    # TODO: Read the version from the file
    # TODO: Parse the version and bump according to bump_type
    # TODO: Write the new version back to the file
    # TODO: Return success/failure and new version
    pass

def build_package(package_dir: Path) -> Tuple[bool, Dict[str, Path]]:
    """
    Build a Python package (source dist and wheel).
    
    Args:
        package_dir: Directory containing the package
        
    Returns:
        Tuple of (success, paths to built distributions)
    """
    # TODO: Run python -m build
    # TODO: Find the built distributions
    # TODO: Return success/failure and paths
    pass

def upload_to_testpypi(dist_files: Dict[str, Path]) -> Tuple[bool, str]:
    """
    Upload a package to TestPyPI.
    
    Args:
        dist_files: Dictionary with paths to distribution files
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Run twine upload to TestPyPI
    # TODO: Return success/failure and message
    pass

def upload_to_pypi(dist_files: Dict[str, Path]) -> Tuple[bool, str]:
    """
    Upload a package to PyPI.
    
    Args:
        dist_files: Dictionary with paths to distribution files
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Run twine upload to PyPI
    # TODO: Return success/failure and message
    pass

def create_github_release(tag: str, release_notes: str) -> Tuple[bool, str]:
    """
    Create a GitHub release.
    
    Args:
        tag: Release tag (e.g. 'v1.0.0')
        release_notes: Release notes
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Use the GitHub CLI or API to create a release
    # TODO: Return success/failure and message
    pass

def setup_github_workflow(project_dir: Path) -> Tuple[bool, str]:
    """
    Set up a GitHub workflow for package publishing.
    
    Args:
        project_dir: Project directory
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Create .github/workflows directory
    # TODO: Create workflow file for package publishing
    # TODO: Return success/failure and message
    pass

class PackagePublisher:
    """A class to manage package publishing."""
    
    def __init__(self, package_dir: Path):
        """
        Initialize the package publisher.
        
        Args:
            package_dir: Directory containing the package
        """
        self.package_dir = package_dir
        # TODO: Validate package structure
    
    def prepare_release(self, bump_type: str = "patch") -> Tuple[bool, Dict[str, Any]]:
        """
        Prepare a package for release.
        
        Args:
            bump_type: Type of version bump ('major', 'minor', 'patch')
            
        Returns:
            Tuple of (success, release_info)
        """
        # TODO: Bump version
        # TODO: Update changelog
        # TODO: Build distributions
        # TODO: Return success/failure and release info
        pass
    
    def publish(self, test: bool = True) -> Tuple[bool, str]:
        """
        Publish the package.
        
        Args:
            test: Whether to publish to TestPyPI (True) or PyPI (False)
            
        Returns:
            Tuple of (success, message)
        """
        # TODO: Build the package if not already built
        # TODO: Upload to TestPyPI or PyPI based on the test flag
        # TODO: Return success/failure and message
        pass
    
    def create_release(self, tag_prefix: str = "v") -> Tuple[bool, str]:
        """
        Create a GitHub release for the package.
        
        Args:
            tag_prefix: Prefix for the version tag
            
        Returns:
            Tuple of (success, message)
        """
        # TODO: Get the current version
        # TODO: Create a tag with the prefix
        # TODO: Generate release notes
        # TODO: Create the GitHub release
        # TODO: Return success/failure and message
        pass

if __name__ == "__main__":
    # Example usage
    print("Python Package Publisher")
    print("----------------------")
    
    # Check package structure if requested
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        package_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        
        is_valid, issues = check_package_structure(package_dir)
        
        if is_valid:
            print("✓ Package structure is valid for publishing")
        else:
            print("✗ Package structure has issues:")
            for issue in issues:
                print(f"  - {issue}")
    
    # Build package if requested
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        package_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        
        success, dist_files = build_package(package_dir)
        
        if success:
            print("✓ Package built successfully:")
            for dist_type, path in dist_files.items():
                print(f"  - {dist_type}: {path}")
        else:
            print("✗ Failed to build package")
    
    # Publish package if requested
    if len(sys.argv) > 1 and sys.argv[1] == "publish":
        package_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        test = sys.argv[3].lower() != "false" if len(sys.argv) > 3 else True
        
        publisher = PackagePublisher(package_dir)
        success, message = publisher.publish(test)
        
        print(message)
    
    # Full release process if requested
    if len(sys.argv) > 1 and sys.argv[1] == "release":
        package_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
        bump_type = sys.argv[3] if len(sys.argv) > 3 else "patch"
        
        publisher = PackagePublisher(package_dir)
        
        print("1. Preparing release...")
        success, release_info = publisher.prepare_release(bump_type)
        
        if success:
            print(f"✓ Release prepared: {release_info.get('version', 'unknown')}")
            
            print("\n2. Publishing to TestPyPI...")
            success, message = publisher.publish(test=True)
            print(message)
            
            if success and input("\nPublish to PyPI? (y/n): ").lower() == "y":
                print("\n3. Publishing to PyPI...")
                success, message = publisher.publish(test=False)
                print(message)
                
                if success:
                    print("\n4. Creating GitHub release...")
                    success, message = publisher.create_release()
                    print(message)
        else:
            print(f"✗ Failed to prepare release: {release_info.get('error', 'unknown error')}")
