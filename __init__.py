"""
Snakers - Interactive Python exercises with Ruff linting.

A learning tool inspired by Rustlings that helps you learn Python
by fixing and completing code exercises.
"""

__version__ = "0.1.0"
__author__ = "Arman Rostami"
__email__ = "arman.rostami@outlook.com"

from runner import ExerciseRunner
from .exercise import Exercise

__all__ = ["ExerciseRunner", "Exercise", "__version__"]
