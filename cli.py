"""
Command line interface for Snakers.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from runner import ExerciseRunner

console = Console()

def print_welcome():
    """Print welcome message and instructions."""
    welcome_text = Text()
    welcome_text.append("🐍 Welcome to ", style="bold blue")
    welcome_text.append("Snakers", style="bold green")
    welcome_text.append("! 🐍\n\n", style="bold blue")
    welcome_text.append("Learn Python by fixing and completing code exercises.\n")
    welcome_text.append("Each exercise uses Ruff for linting and style checking.\n\n")
    welcome_text.append("Commands:\n", style="bold")
    welcome_text.append("  run [exercise]  - Run next exercise or specific exercise\n")
    welcome_text.append("  watch          - Watch for file changes and auto-check\n")
    welcome_text.append("  list           - List all exercises with progress\n")
    welcome_text.append("  reset          - Reset progress\n")
    welcome_text.append("  help           - Show this help message\n")
    
    console.print(Panel(welcome_text, title="Snakers", border_style="green"))

def main(exercises_dir: Optional[Path] = None):
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Snakers - Interactive Python exercises with Ruff linting",
        prog="snakers"
    )
    parser.add_argument(
        "command", 
        nargs="?", 
        default="help", 
        choices=["run", "watch", "list", "reset", "help"],
        help="Command to execute"
    )
    parser.add_argument(
        "exercise", 
        nargs="?", 
        help="Specific exercise name (for run command)"
    )
    parser.add_argument(
        "--exercises-dir",
        type=Path,
        default=exercises_dir,
        help="Directory containing exercises"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"snakers {__import__('snakers').__version__}"
    )
    
    args = parser.parse_args()
    
    if args.command == "help":
        print_welcome()
        return
    
    # Initialize runner with exercises directory
    if args.exercises_dir and args.exercises_dir.exists():
        runner = ExerciseRunner(args.exercises_dir)
    else:
        console.print("[red]Error: Exercises directory not found.[/red]")
        console.print(f"Looking for: {args.exercises_dir}")
        sys.exit(1)
    
    try:
        if args.command == "run":
            runner.run_exercise(args.exercise)
        elif args.command == "watch":
            runner.watch_mode(args.exercise)
        elif args.command == "list":
            runner.list_exercises()
        elif args.command == "reset":
            runner.reset_progress()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
