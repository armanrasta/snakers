"""
Initialization module for Snakers.

This module handles creating the initial directory structure and exercise files.
"""

import shutil
from pathlib import Path

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

        # Find source exercise files
        package_dir = Path(__file__).parent
        exercises_dir = package_dir / "exercises"

        if exercises_dir.exists() and any(exercises_dir.glob("**/*.py")):
            # Copy from actual exercises directory
            source_dir = exercises_dir
            console.print("[green]Using existing exercise files...[/green]")
        else:
            # Fall back to templates or create them
            template_dir = package_dir / "templates"
            if not template_dir.exists() or not any(template_dir.glob("**/*.py")):
                console.print("[yellow]No exercise files found. Creating templates...[/yellow]")
                create_template_directory()
            source_dir = template_dir

        # Count exercise files to copy
        exercise_files = list(source_dir.glob("**/*.py")) + list(source_dir.glob("**/*.md"))

        if not exercise_files:
            console.print("[red]Error: No exercise files found.[/red]")
            console.print("Directories have been created. You may need to add exercise files manually.")
            return

        console.print(f"[green]Found {len(exercise_files)} exercise files to copy.[/green]")
        copy_task = progress.add_task("[bold blue]Copying exercise files...", total=len(exercise_files))

        for source_file in exercise_files:
            # Determine target location preserving directory structure
            rel_path = source_file.relative_to(source_dir)
            dest_path = target_dir / "exercises" / rel_path

            # Create parent directories if needed
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            # Copy the file
            shutil.copy2(source_file, dest_path)
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

        # Skip the my_package directory since it's a subdirectory
        if "my_package" in directory:
            continue

        # Extract category from directory path
        category = directory.split("/")[1]

        # Create directory in templates
        category_dir = template_dir / category
        category_dir.mkdir(exist_ok=True)

        # Create a sample exercise file
        sample_file = category_dir / "01_sample.py"
        with open(sample_file, "w") as f:
            f.write(f"""# filepath: /exercises/{category}/01_sample.py
\"\"\"
Exercise: Sample {category.replace('_', ' ').title()} Exercise

This is a sample exercise for the {category} category.

Tasks:
1. Implement the sample_function
2. Make sure it returns a proper value
3. Run the tests to verify your implementation

Hints:
- Read the docstring for guidance
- Return a simple string as a first step
\"\"\"

def sample_function():
    \"\"\"A sample function that needs to be implemented.

    Returns:
        str: A greeting message
    \"\"\"
    # TODO: Implement this function
    pass

if __name__ == "__main__":
    # Test the function
    result = sample_function()
    print(f"Result: {{result}}")

    # Check if the function returns a non-empty string
    assert result, "Function should return a non-empty value"
    assert isinstance(result, str), "Function should return a string"
    print("All tests passed!")
""")

        # Create a README.md for the category
        readme_file = category_dir / "README.md"
        with open(readme_file, "w") as f:
            f.write(f"""# {category.replace('_', ' ').title()} Exercises

These exercises will help you learn and practice {category.replace('_', ' ')} concepts in Python.

## Getting Started

Run the first exercise:

```bash
snakers run {category}/01_sample
```

Or watch for file changes:

```bash
snakers watch {category}/01_sample
```

## Topics Covered

- Basic {category.replace('_', ' ')} concepts
- Common {category.replace('_', ' ')} operations
- Best practices for {category.replace('_', ' ')}
""")

    # Create special case for my_package directory
    if "09_modules_packages/my_package" in DIRECTORY_STRUCTURE:
        my_package_dir = template_dir / "09_modules_packages" / "my_package"
        my_package_dir.mkdir(exist_ok=True, parents=True)

        # Create __init__.py
        with open(my_package_dir / "__init__.py", "w") as f:
            f.write("""# filepath: /exercises/09_modules_packages/my_package/__init__.py
\"\"\"
Sample package for modules and packages exercises.
\"\"\"

# TODO: Import and expose modules here
""")

        # Create a module file
        with open(my_package_dir / "functions.py", "w") as f:
            f.write("""# filepath: /exercises/09_modules_packages/my_package/functions.py
\"\"\"
Utility functions for the sample package.
\"\"\"

def add(a, b):
    \"\"\"Add two numbers.\"\"\"
    # TODO: Implement this function
    pass

def multiply(a, b):
    \"\"\"Multiply two numbers.\"\"\"
    # TODO: Implement this function
    pass
""")

    console.print(f"[bold green]Template directory created at {template_dir}[/bold green]")
    console.print(f"[green]Created {len(list(template_dir.glob('**/*.py')))} Python files[/green]")

if __name__ == "__main__":
    # This can be run directly to create the template directory
    create_template_directory()
