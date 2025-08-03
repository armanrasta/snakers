"""
Exercise class for handling individual exercises.
"""

import subprocess
import sys
from pathlib import Path
from typing import Optional

from rich.console import Console

console = Console()

class Exercise:
    """Represents a single exercise."""
    
    def __init__(self, path: Path):
        self.path = path
        self.name = path.stem
        self.relative_path = str(path.relative_to(path.parent.parent))
    
    def get_content(self) -> str:
        """Get the exercise file content."""
        return self.path.read_text()
    
    def check(self) -> bool:
        """Check if the exercise passes all validation."""
        # Check for TODO comments
        content = self.get_content()
        if "# TODO" in content or "# FIXME" in content:
            console.print(f"[yellow]Exercise {self.name} still has TODO items[/yellow]")
            return False
        
        # Run ruff check
        if not self._run_ruff_check():
            return False
        
        # Run the file
        if not self._run_file():
            return False
        
        console.print(f"[green]✅ {self.name} passed all checks![/green]")
        return True
    
    def _run_ruff_check(self) -> bool:
        """Run ruff check on the exercise."""
        try:
            result = subprocess.run(
                ["ruff", "check", str(self.path)],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                console.print(f"[red]Ruff check failed for {self.name}:[/red]")
                console.print(result.stdout + result.stderr)
                return False
            return True
        except FileNotFoundError:
            console.print("[red]Error: Ruff not found. Please install ruff.[/red]")
            return False
    
    def _run_file(self) -> bool:
        """Run the exercise file."""
        try:
            result = subprocess.run(
                [sys.executable, str(self.path)],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode != 0:
                console.print(f"[red]Runtime error in {self.name}:[/red]")
                console.print(result.stdout + result.stderr)
                return False
            return True
        except subprocess.TimeoutExpired:
            console.print(f"[red]Timeout: {self.name} took too long to run[/red]")
            return False
        except Exception as e:
            console.print(f"[red]Error running {self.name}: {e}[/red]")
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
