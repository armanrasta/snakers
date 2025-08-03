"""
Example package for learning about Python packages.

This is the __init__.py file that makes my_package a proper package.

This file can also define package-level variables and import submodules.
"""

__version__ = "0.1.0"
__author__ = "Snacker"

from .utils import add, subtract
from .math_functions import square, cube

__all__ = ["add", "subtract", "square", "cube"]
