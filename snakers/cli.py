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

from .runner import ExerciseRunner
from .init import initialize_snakers

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
    welcome_text.append("  init            - Initialize or reset exercises directory\n")
    welcome_text.append("  solutions       - Manage solutions (list, show, reset)\n")
    welcome_text.append("  help [topic]    - Show help on a specific topic\n")
    
    console.print(Panel(welcome_text, title="Snakers", border_style="green"))

def print_help(topic: Optional[str] = None):
    """Print help information on a specific topic."""
    if topic is None:
        print_welcome()
        return
    
    # Help topics
    topics = {
        "init": (
            "Initialize Snakers",
            "Creates the necessary directory structure and exercise files.\n\n"
            "Usage: snakers init [--target DIR]\n\n"
            "Options:\n"
            "  --target DIR  Directory to initialize (default: current directory)\n\n"
            "This will create:\n"
            "- An exercises directory with all exercise files\n"
            "- A solutions directory to store completed exercises\n"
            "- Initial configuration files"
        ),
        # ...existing help topics...
    }
    
    if topic in topics:
        title, content = topics[topic]
        console.print(Panel(content, title=title, border_style="blue"))
    else:
        console.print(f"[yellow]No help available for topic '{topic}'[/yellow]")
        console.print("Available topics:")
        for available_topic in topics:
            console.print(f"  - {available_topic}")

def main(exercises_dir: Optional[Path] = None):
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Snakers - Interactive Python exercises with Ruff linting",
        prog="snakers"
    )
    
    # Main subparsers
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Init command
    init_parser = subparsers.add_parser("init", help="Initialize exercises")
    init_parser.add_argument("--target", type=Path, help="Target directory for initialization")
    
    # Run command
    run_parser = subparsers.add_parser("run", help="Run an exercise")
    run_parser.add_argument("exercise", nargs="?", help="Specific exercise name")
    
    # Watch command
    watch_parser = subparsers.add_parser("watch", help="Watch for file changes")
    watch_parser.add_argument("exercise", nargs="?", help="Specific exercise name")
    
    # List command
    subparsers.add_parser("list", help="List all exercises with progress")
    
    # Reset command
    subparsers.add_parser("reset", help="Reset progress")
    
    # Solutions subcommand
    solutions_parser = subparsers.add_parser("solutions", help="Manage solutions")
    solutions_subparsers = solutions_parser.add_subparsers(dest="solutions_command", help="Solutions command")
    
    # Solutions list command
    solutions_subparsers.add_parser("list", help="List all solutions")
    
    # Solutions show command
    show_parser = solutions_subparsers.add_parser("show", help="Show a specific solution")
    show_parser.add_argument("exercise", help="Exercise name to show solution for")
    
    # Solutions reset command
    solutions_subparsers.add_parser("reset", help="Reset all solutions")
    
    # Help command
    help_parser = subparsers.add_parser("help", help="Show help message")
    help_parser.add_argument("topic", nargs="?", help="Help topic")
    
    # Version flag
    parser.add_argument(
        "--version",
        action="version",
        version=f"snakers 0.1.0"  # Hardcoded version for now
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    if args.command == "help":
        print_help(args.topic)
        return
    
    if args.command is None:
        print_welcome()
        return
    
    if args.command == "init":
        target_dir = args.target or Path.cwd()
        initialize_snakers(target_dir)
        return
    
    # Initialize runner with exercises directory
    if exercises_dir and exercises_dir.exists():
        runner = ExerciseRunner(exercises_dir)
    else:
        console.print("[red]Error: Exercises directory not found.[/red]")
        console.print(f"Looking for: {exercises_dir}")
        console.print("[yellow]Try running 'snakers init' to create the exercises directory.[/yellow]")
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
        elif args.command == "solutions":
            if args.solutions_command == "list":
                runner.list_solutions()
            elif args.solutions_command == "show":
                runner.show_solution(args.exercise)
            elif args.solutions_command == "reset":
                runner.reset_solutions()
            else:
                console.print("[yellow]Please specify a solutions command (list, show, reset)[/yellow]")
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)
