"""
Main entry point for snakers package.

This allows the package to be executed with:
    python -m snakers
"""

import sys
from pathlib import Path
from .cli import main

# Add the package's exercises directory to the path
PACKAGE_DIR = Path(__file__).parent
EXERCISES_DIR = PACKAGE_DIR / "exercises"

def run():
    """Entry point for the snakers command."""
    main(exercises_dir=EXERCISES_DIR)

if __name__ == "__main__":
    run()
