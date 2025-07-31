"""
Exercise 1.2: Constants and Naming Conventions

Learn about Python constants, naming conventions, and immutable values.

Tasks:
1. Define constants following Python conventions
2. Understand when to use constants vs variables
3. Practice with Final type hints

Topics covered:
- Constant naming (UPPER_CASE)
- Final type hint from typing
- Module-level constants
- Enum for related constants
"""

from typing import Final
from enum import Enum

# TODO: Define a constant for maximum file size (10MB in bytes)
# TODO: Define a constant for application name "Snakers"
# TODO: Define a constant for version number "1.0.0"
# TODO: Define a constant for default timeout (30 seconds)

class Priority(Enum):
    """Priority levels for tasks"""
    # TODO: Define enum values: LOW=1, MEDIUM=2, HIGH=3, CRITICAL=4
    pass

class Config:
    """Configuration class with typed constants"""
    
    # TODO: Add class-level constants with Final type hints
    # TODO: DATABASE_URL: Final[str] = "sqlite:///snakers.db"
    # TODO: DEBUG_MODE: Final[bool] = False
    # TODO: MAX_RETRIES: Final[int] = 3
    
    @classmethod
    def get_database_url(cls) -> str:
        """Get database URL with environment override"""
        import os
        # TODO: Return DATABASE_URL or environment variable 'DATABASE_URL'
        pass
    
    @classmethod
    def is_debug_enabled(cls) -> bool:
        """Check if debug mode is enabled"""
        import os
        # TODO: Return DEBUG_MODE or check 'DEBUG' environment variable
        pass

def calculate_max_items(item_size: int) -> int:
    """Calculate maximum items that fit in max file size"""
    # TODO: Use the MAX_FILE_SIZE constant
    # TODO: Return max_file_size // item_size
    # TODO: Handle division by zero
    pass

if __name__ == "__main__":
    print(f"App: {APP_NAME} v{VERSION}")
    print(f"Max file size: {MAX_FILE_SIZE} bytes")
    print(f"Default timeout: {DEFAULT_TIMEOUT} seconds")
    
    # Test enum
    task_priority = Priority.HIGH
    print(f"Task priority: {task_priority.name} ({task_priority.value})")
    
    # Test config
    print(f"Database URL: {Config.get_database_url()}")
    print(f"Debug enabled: {Config.is_debug_enabled()}")
