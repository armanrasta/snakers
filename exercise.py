"""
Exercise class for handling individual exercise files.
"""

import subprocess
import sys
from pathlib import Path
from typing import Optional

from rich.console import Console

console = Console()

class Exercise:
    """Represents a single exercise file."""
    
    def __init__(self, path: Path):
        self.path = path
        self.name = path.stem
        # Calculate relative path from exercises directory
        parts = path.parts
        if "exercises" in parts:
            exercises_idx = parts.index("exercises")
            self.relative_path = "/".join(parts[exercises_idx:])
        else:
            self.relative_path = str(path)
    
    def get_content(self) -> str:
        """Get the content of the exercise file."""
        try:
            return self.path.read_text(encoding="utf-8")
        except IOError as e:
            console.print(f"[red]Error reading file {self.path}: {e}[/red]")
            return ""
    
    def has_todos(self) -> bool:
        """Check if exercise still has TODO comments."""
        content = self.get_content()
        return "# TODO" in content or "# FIXME" in content
    
    def run_ruff_check(self) -> tuple[bool, str]:
        """Run ruff check on the exercise file."""
        try:
            result = subprocess.run(
                ["ruff", "check", str(self.path)],
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.returncode == 0, result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return False, "Ruff check timed out"
        except FileNotFoundError:
            console.print("[red]Error: Ruff not found. Please install ruff: pip install ruff[/red]")
            return False, "Ruff not installed"
        except Exception as e:
            return False, f"Error running ruff: {e}"
    
    def run_python_file(self) -> tuple[bool, str]:
        """Run the Python file to check for runtime errors."""
        try:
            result = subprocess.run(
                [sys.executable, str(self.path)],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=self.path.parent
            )
            return result.returncode == 0, result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return False, "Exercise execution timed out"
        except Exception as e:
            return False, f"Error running exercise: {e}"
    
    def check(self) -> bool:
        """Check if the exercise passes all requirements."""
        # Check for incomplete TODOs
        if self.has_todos():
            console.print(f"[yellow]📝 Exercise '{self.name}' still has TODO items to complete[/yellow]")
            return False
        
        # Run ruff check
        ruff_passed, ruff_output = self.run_ruff_check()
        if not ruff_passed:
            console.print(f"[red]❌ Ruff check failed for '{self.name}':[/red]")
            if ruff_output.strip():
                console.print(ruff_output)
            return False
        
        # Run the exercise
        run_passed, run_output = self.run_python_file()
        if not run_passed:
            console.print(f"[red]❌ Runtime error in '{self.name}':[/red]")
            if run_output.strip():
                console.print(run_output)
            return False
        
        console.print(f"[green]✅ '{self.name}' passed all checks![/green]")
        if run_output.strip():
            console.print("[dim]Output:[/dim]")
            console.print(run_output)
        
        return True
