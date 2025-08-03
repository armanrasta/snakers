#!/usr/bin/env python3
"""
Snakers - Interactive Python exercises with Ruff linting

This is a simple entry point script to run the Snakers package.
"""

from snakers.cli import main

if __name__ == "__main__":
    main()
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
import subprocess
from typing import List, Optional
from pathlib import Path
import json

console = Console()

class ExerciseRunner:
    def __init__(self, exercise_dir: Path = Path("exercises")):
        self.exercise_dir = exercise_dir
        self.progress_file = Path(".snakers_progress.json")
        self.progress = self.load_progress()
    
    def load_progress(self) -> dict:
        if self.progress_file.exists():
            with open(self.progress_file) as f:
                return json.load(f)
        return {"completed": []}
    
    def save_progress(self):
        with open(self.progress_file, "w") as f:
            json.dump(self.progress, f, indent=2)
    
    def get_exercises(self) -> List[Path]:
        """Get all exercise files sorted by name"""
        return sorted(self.exercise_dir.glob("**/*.py"))
    
    def run_ruff_check(self, file_path: Path) -> tuple[bool, str]:
        """Run ruff check on a file"""
        try:
            result = subprocess.run(
                ["ruff", "check", str(file_path)],
                capture_output=True,
                text=True
            )
            return result.returncode == 0, result.stdout + result.stderr
        except FileNotFoundError:
            console.print("[red]Error: Ruff not found. Please install ruff.[/red]")
            sys.exit(1)
    
    def run_python_file(self, file_path: Path) -> tuple[bool, str]:
        """Run the Python file to check for runtime errors"""
        try:
            result = subprocess.run(
                [sys.executable, str(file_path)],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0, result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return False, "Timeout: Exercise took too long to run"
        except Exception as e:
            return False, f"Error running file: {e}"
    
    def check_exercise(self, file_path: Path) -> bool:
        """Check if an exercise passes all checks"""
        # Check for TODO comments (exercise not completed)
        content = file_path.read_text()
        if "# TODO" in content or "# FIXME" in content:
            console.print(f"[yellow]Exercise {file_path.name} still has TODO items[/yellow]")
            return False
        
        # Run ruff check
        ruff_passed, ruff_output = self.run_ruff_check(file_path)
        if not ruff_passed:
            console.print(f"[red]Ruff check failed for {file_path.name}:[/red]")
            console.print(ruff_output)
            return False
        
        # Run the file
        run_passed, run_output = self.run_python_file(file_path)
        if not run_passed:
            console.print(f"[red]Runtime error in {file_path.name}:[/red]")
            console.print(run_output)
            return False
        
        console.print(f"[green]✓ {file_path.name} passed all checks![/green]")
        return True
    
    def run_exercise(self, exercise_name: Optional[str] = None):
        """Run a specific exercise or the next incomplete one"""
        exercises = self.get_exercises()
        
        if exercise_name:
            exercise_file = self.exercise_dir / f"{exercise_name}.py"
            if not exercise_file.exists():
                console.print(f"[red]Exercise '{exercise_name}' not found[/red]")
                return
            target_exercise = exercise_file
        else:
            # Find next incomplete exercise
            completed = set(self.progress["completed"])
            target_exercise = None
            for ex in exercises:
                if ex.name not in completed:
                    target_exercise = ex
                    break
            
            if not target_exercise:
                console.print("[green]🎉 All exercises completed![/green]")
                return
        
        console.print(Panel(f"Working on: [bold]{target_exercise.name}[/bold]"))
        
        # Show exercise content
        content = target_exercise.read_text()
        syntax = Syntax(content, "python", theme="monokai", line_numbers=True)
        console.print(syntax)
        
        if self.check_exercise(target_exercise):
            if target_exercise.name not in self.progress["completed"]:
                self.progress["completed"].append(target_exercise.name)
                self.save_progress()
    
    def watch_mode(self, exercise_name: Optional[str] = None):
        """Watch for file changes and auto-check exercises"""
        console.print("[blue]👀 Watching for changes... (Ctrl+C to exit)[/blue]")
        
        class ChangeHandler(FileSystemEventHandler):
            def __init__(self, runner):
                self.runner = runner
            
            def on_modified(self, event):
                if str(event.src_path).endswith('.py') and not event.is_directory:
                    file_path = Path(str(event.src_path))
                    console.print(f"\n[cyan]File changed: {file_path.name}[/cyan]")
                    self.runner.check_exercise(file_path)
        
        event_handler = ChangeHandler(self)
        observer = Observer()
        observer.schedule(event_handler, str(self.exercise_dir), recursive=True)
        observer.start()
        
        try:
            observer.join()
        except KeyboardInterrupt:
            observer.stop()
            console.print("\n[yellow]Stopped watching[/yellow]")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Snakers Python exercises")
    parser.add_argument("command", nargs="?", default="run", 
                       choices=["run", "watch", "list", "reset"])
    parser.add_argument("exercise", nargs="?", help="Specific exercise name")
    
    args = parser.parse_args()
    runner = ExerciseRunner()
    
    if args.command == "run":
        runner.run_exercise(args.exercise)
    elif args.command == "watch":
        runner.watch_mode(args.exercise)
    elif args.command == "list":
        exercises = runner.get_exercises()
        completed = set(runner.progress["completed"])
        for ex in exercises:
            status = "✓" if ex.name in completed else "○"
            console.print(f"{status} {ex.name}")
    elif args.command == "reset":
        runner.progress = {"completed": []}
        runner.save_progress()
        console.print("[yellow]Progress reset[/yellow]")

if __name__ == "__main__":
    main()
