"""
Exercise 1.3: Advanced Variable Types

Learn about complex variable types and modern Python typing features.

Tasks:
1. Work with Union, Optional, and Literal types
2. Use TypeVar and Generic types
3. Understand NewType and type aliases

Topics covered:
- Union and Optional types
- Literal types for specific values
- TypeVar for generic programming
- NewType for type safety
- Type aliases for readability
"""

from typing import Union, Optional, Literal, TypeVar, Generic, NewType
from dataclasses import dataclass

# TODO: Create type aliases
# TODO: UserId = NewType('UserId', int)
# TODO: EmailAddress = NewType('EmailAddress', str)
# TODO: JsonValue = Union[str, int, float, bool, None, list, dict]

T = TypeVar('T')
StatusType = Literal['pending', 'processing', 'completed', 'failed']

@dataclass
class User:
    """User dataclass with advanced typing"""
    # TODO: Add fields with proper type hints:
    # TODO: user_id: UserId
    # TODO: email: EmailAddress
    # TODO: name: str
    # TODO: age: Optional[int] = None
    # TODO: status: StatusType = 'pending'
    pass

class Container(Generic[T]):
    """Generic container class"""
    
    def __init__(self, value: T) -> None:
        # TODO: Store the value with proper typing
        pass
    
    def get_value(self) -> T:
        """Return the stored value"""
        # TODO: Return the stored value
        pass
    
    def set_value(self, value: T) -> None:
        """Set a new value"""
        # TODO: Set the new value with type checking
        pass

def process_json_data(data: JsonValue) -> str:
    """Process JSON data and return string representation"""
    # TODO: Handle different JSON value types
    # TODO: Use isinstance() to check types
    # TODO: Return appropriate string representation
    pass

def create_user(
    user_id: int,
    email: str,
    name: str,
    age: Optional[int] = None
) -> User:
    """Create a user with proper type conversion"""
    # TODO: Convert int to UserId using NewType
    # TODO: Convert str to EmailAddress using NewType
    # TODO: Create and return User instance
    pass

def update_user_status(user: User, status: StatusType) -> User:
    """Update user status with validation"""
    # TODO: Validate status is one of the allowed literal values
    # TODO: Update user status
    # TODO: Return updated user
    pass

if __name__ == "__main__":
    # Test NewType usage
    user = create_user(123, "user@example.com", "John Doe", 25)
    print(f"Created user: {user}")
    
    # Test status update
    updated_user = update_user_status(user, "completed")
    print(f"Updated user: {updated_user}")
    
    # Test generic container
    int_container = Container[int](42)
    str_container = Container[str]("hello")
    
    print(f"Int container: {int_container.get_value()}")
    print(f"String container: {str_container.get_value()}")
    
    # Test JSON processing
    json_values = [42, "hello", [1, 2, 3], {"key": "value"}, None]
    for value in json_values:
        result = process_json_data(value)
        print(f"JSON {type(value).__name__}: {result}")
