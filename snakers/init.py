"""
Initialization module for Snakers.

This module handles creating the initial directory structure and exercise files.
"""

import os
import shutil
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

console = Console()

# Define the basic directory structure
DIRECTORY_STRUCTURE = [
    "exercises/00_intro",
    "exercises/01_variables",
    "exercises/02_collections",
    "exercises/03_functions",
    "exercises/04_control_flow",
    "exercises/05_exceptions",
    "exercises/06_classes",
    "exercises/07_functional",
    "exercises/08_file_io",
    "exercises/09_modules_packages",
    "exercises/09_modules_packages/my_package",
    "exercises/10_advanced",
    "exercises/11_testing",
    "exercises/12_concurrency",
    "exercises/13_data",
    "exercises/14_web",
    "exercises/15_stdlib",
    "exercises/16_project_management",
    "exercises/17_design_patterns",
    "exercises/18_regex",
    "solutions"
]

def initialize_snakers(target_dir: Path) -> None:
    """
    Initialize the Snakers directory structure and copy exercise files.
    
    Args:
        target_dir: Target directory for initialization
    """
    console.print(f"[bold green]Initializing Snakers in {target_dir}[/bold green]")
    
    # Create directory structure
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        TextColumn("[bold green]{task.completed}/{task.total}"),
        console=console
    ) as progress:
        # Create directories task
        dir_task = progress.add_task("[bold blue]Creating directories...", total=len(DIRECTORY_STRUCTURE))
        
        for directory in DIRECTORY_STRUCTURE:
            dir_path = target_dir / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            progress.update(dir_task, advance=1)
        
        # Copy exercise files task
        package_dir = Path(__file__).parent
        template_dir = package_dir / "templates"
        
        if not template_dir.exists():
            console.print("[yellow]Warning: Template directory not found. Skipping file creation.[/yellow]")
            console.print("Directories have been created. You can add exercise files manually.")
            return
        
        # Count exercise files to copy
        exercise_files = list(template_dir.glob("**/*.py")) + list(template_dir.glob("**/*.md"))
        
        copy_task = progress.add_task("[bold blue]Copying exercise files...", total=len(exercise_files))
        
        for template_file in exercise_files:
            rel_path = template_file.relative_to(template_dir)
            dest_path = target_dir / "exercises" / rel_path
            
            # Create parent directories if needed
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy the file
            shutil.copy2(template_file, dest_path)
            progress.update(copy_task, advance=1)
    
    # Create a README file
    readme_path = target_dir / "README.md"
    if not readme_path.exists():
        with open(readme_path, "w") as f:
            f.write("""# Snakers - Python Learning Exercises

A collection of Python exercises inspired by Rustlings.

## Getting Started

1. Run exercises with:
   ```
   python -m snakers run
   ```

2. Watch for changes:
   ```
   python -m snakers watch
   ```

3. View your progress:
   ```
   python -m snakers list
   ```

4. Get help:
   ```
   python -m snakers help
   ```

Happy coding! 🐍
""")
    
    console.print("[bold green]✅ Snakers initialized successfully![/bold green]")
    console.print("\nTo get started, try running: [bold]python -m snakers run[/bold]")

def create_template_directory():
    """
    Create a template directory with sample exercise files.
    This is used for development and packaging purposes.
    """
    package_dir = Path(__file__).parent
    template_dir = package_dir / "templates"
    
    # Create the template directory if it doesn't exist
    template_dir.mkdir(exist_ok=True)
    
    # Create a sample exercise file for each directory
    for directory in DIRECTORY_STRUCTURE:
        if not directory.startswith("exercises/"):
            continue
            
        # Extract category from directory path
        category = directory.split("/")[1]
        
        # Create directory in templates
        category_dir = template_dir / category
        category_dir.mkdir(exist_ok=True)
        
        # Create a sample exercise file
        sample_file = category_dir / f"01_sample.py"
        with open(sample_file, "w") as f:
            f.write(f"""# filepath: /exercises/{category}/01_sample.py
\"\"\"
Exercise: Sample {category.replace('_', ' ').title()} Exercise

This is a sample exercise for the {category} category.
\"\"\"

def sample_function():
    \"\"\"A sample function that needs to be implemented.\"\"\"
    # TODO: Implement this function
    pass

if __name__ == "__main__":
    # Test the function
    sample_function()
""")
    
    console.print(f"[bold green]Template directory created at {template_dir}[/bold green]")

if __name__ == "__main__":
    # This can be run directly to create the template directory
    create_template_directory()