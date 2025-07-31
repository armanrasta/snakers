"""
Exercise runner and progress tracking.
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .snakers.exercise import Exercise

console = Console()

class ExerciseRunner:
    """Manages exercise execution and progress tracking."""
    
    def __init__(self, exercise_dir: Path):
        self.exercise_dir = exercise_dir
        self.progress_file = Path.home() / ".snakers_progress.json"
        self.progress = self.load_progress()
    
    def load_progress(self) -> dict:
        """Load progress from file."""
        if self.progress_file.exists():
            try:
                with open(self.progress_file) as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                console.print("[yellow]Warning: Could not load progress file[/yellow]")
        return {"completed": [], "version": "0.1.0"}
    
    def save_progress(self):
        """Save progress to file."""
        try:
            with open(self.progress_file, "w") as f:
                json.dump(self.progress, f, indent=2)
        except IOError as e:
            console.print(f"[yellow]Warning: Could not save progress: {e}[/yellow]")
    
    def get_exercises(self) -> List[Exercise]:
        """Get all exercise files sorted by path."""
        exercise_files = sorted(self.exercise_dir.glob("**/*.py"))
        return [Exercise(path) for path in exercise_files]
    
    def run_exercise(self, exercise_name: Optional[str] = None):
        """Run a specific exercise or the next incomplete one."""
        exercises = self.get_exercises()
        
        if not exercises:
            console.print("[yellow]No exercises found in the exercises directory.[/yellow]")
            return
        
        if exercise_name:
            # Find specific exercise
            target_exercise = None
            for ex in exercises:
                if ex.name == exercise_name or ex.path.stem == exercise_name:
                    target_exercise = ex
                    break
            
            if not target_exercise:
                console.print(f"[red]Exercise '{exercise_name}' not found[/red]")
                self.list_exercises()
                return
        else:
            # Find next incomplete exercise
            completed = set(self.progress["completed"])
            target_exercise = None
            for ex in exercises:
                if ex.relative_path not in completed:
                    target_exercise = ex
                    break
            
            if not target_exercise:
                console.print("[green]🎉 Congratulations! All exercises completed![/green]")
                return
        
        self._display_exercise(target_exercise)
        
        if target_exercise.check():
            if target_exercise.relative_path not in self.progress["completed"]:
                self.progress["completed"].append(target_exercise.relative_path)
                self.save_progress()
                console.print(f"[green]✅ Exercise '{target_exercise.name}' completed![/green]")
    
    def _display_exercise(self, exercise: Exercise):
        """Display exercise content and information."""
        console.print(Panel(
            f"[bold]Exercise:[/bold] {exercise.name}\n"
            f"[bold]File:[/bold] {exercise.relative_path}",
            title="Current Exercise",
            border_style="blue"
        ))
        
        # Show exercise content
        content = exercise.get_content()
        syntax = Syntax(content, "python", theme="monokai", line_numbers=True)
        console.print(syntax)
    
    def list_exercises(self):
        """List all exercises with completion status."""
        exercises = self.get_exercises()
        completed = set(self.progress["completed"])
        
        table = Table(title="Snakers Exercises")
        table.add_column("Status", style="green", width=8)
        table.add_column("Exercise", style="cyan")
        table.add_column("File", style="dim")
        
        for ex in exercises:
            status = "✅ Done" if ex.relative_path in completed else "⭕ TODO"
            table.add_row(status, ex.name, str(ex.relative_path))
        
        console.print(table)
        
        completed_count = len([ex for ex in exercises if ex.relative_path in completed])
        total_count = len(exercises)
        console.print(f"\nProgress: {completed_count}/{total_count} exercises completed")
    
    def reset_progress(self):
        """Reset all progress."""
        self.progress = {"completed": [], "version": "0.1.0"}
        self.save_progress()
        console.print("[yellow]📝 Progress reset! Starting fresh.[/yellow]")
    
    def watch_mode(self, exercise_name: Optional[str] = None):
        """Watch for file changes and auto-check exercises."""
        console.print("[blue]👀 Watching for changes... (Ctrl+C to exit)[/blue]")
        
        class ChangeHandler(FileSystemEventHandler):
            def __init__(self, runner):
                self.runner = runner
            
            def on_modified(self, event):
                if event.src_path.endswith('.py') and not event.is_directory:
                    file_path = Path(event.src_path)
                    if file_path.is_relative_to(self.runner.exercise_dir):
                        exercise = Exercise(file_path)
                        console.print(f"\n[cyan]🔄 File changed: {exercise.name}[/cyan]")
                        if exercise.check():
                            console.print(f"[green]✅ {exercise.name} passed![/green]")
        
        event_handler = ChangeHandler(self)
        observer = Observer()
        observer.schedule(event_handler, str(self.exercise_dir), recursive=True)
        observer.start()
        
        try:
            # Show initial exercise if none specified
            if not exercise_name:
                self.run_exercise()
            observer.join()
        except KeyboardInterrupt:
            observer.stop()
            console.print("\n[yellow]👋 Stopped watching[/yellow]")
