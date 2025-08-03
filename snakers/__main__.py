"""
Main entry point for snakers package.

This allows the package to be executed with:
    python -m snakers
"""

import sys
from pathlib import Path
from .cli import main
from rich.console import Console

# Add the package's exercises directory to the path
PACKAGE_DIR = Path(__file__).parent
EXERCISES_DIR = PACKAGE_DIR / "exercises"

console = Console()

def run():
    """Entry point for the snakers command."""
    # Check if exercises directory exists in package
    if EXERCISES_DIR.exists():
        main(exercises_dir=EXERCISES_DIR)
    else:
        # Look for exercises in current directory
        cwd_exercises = Path.cwd() / "exercises"
        if cwd_exercises.exists():
            main(exercises_dir=cwd_exercises)
        else:
            # No exercises found, run CLI anyway (it will show help or init)
            main()

if __name__ == "__main__":
    run()
