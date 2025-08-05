# Snakers 🐍

Interactive Python exercises with Ruff linting - Learn Python by fixing and completing code!

## Installation

```bash
# Clone the repository
git clone https://github.com/armanrasta/snakers.git
cd snakers

# Install dependencies
pip install -e .
```

## Usage

### Initialize the exercises
```bash
# Create exercises directory and files in current directory
snakers init

# Create in a specific directory
snakers init --target /path/to/directory
```

### Run the next exercise
```bash
# If installed via pip
snakers run

# Or using the module
python -m snakers run
```

### Run a specific exercise
```bash
snakers run 01_variables/01_basic_types
```

### Watch mode (auto-check on file changes)
```bash
snakers watch
```

### List all exercises
```bash
snakers list
```

### Reset progress
```bash
snakers reset
```

### Manage solutions
```bash
# List all saved solutions
snakers solutions list

# View a specific solution
snakers solutions show 01_basic_types

# Reset all solutions
snakers solutions reset
```

### Get help
```bash
# General help
snakers help

# Topic-specific help
snakers help init
snakers help solutions
```

## Exercise Structure

Exercises are organized in the `exercises/` directory by topic:
- `00_intro/` - Introduction and environment setup
- `01_variables/` - Variables, types, basic operations
- `02_collections/` - Lists, dictionaries, tuples, sets
- `03_functions/` - Function definitions, parameters, returns
- `04_control_flow/` - Conditionals, loops, flow control
- `05_exceptions/` - Error handling and exceptions
- `06_classes/` - Object-oriented programming
- `07_functional/` - Functional programming concepts
- `08_file_io/` - File operations and data formats
- `09_modules_packages/` - Imports, packages, modules
- `10_advanced/` - Decorators, generators, advanced concepts
- `11_testing/` - Unit testing and test-driven development
- `12_concurrency/` - Threading, multiprocessing, async programming
- `13_data/` - Data processing and analysis
- `14_web/` - HTTP clients and web programming
- `15_stdlib/` - Standard library modules
- `16_project_management/` - Virtual environments, packaging, project structure
- `17_design_patterns/` - Common design patterns
- `18_regex/` - Regular expressions

Each exercise file contains:
- Learning objectives
- TODO items to complete
- Hints and tips
- Test cases

## How It Works

1. **Find TODOs**: Each exercise has `# TODO` comments marking what you need to implement
2. **Fix the code**: Replace TODOs with working Python code
3. **Pass Ruff checks**: Your code must pass Ruff linting (style, formatting, basic errors)
4. **Run successfully**: The exercise file must execute without runtime errors
5. **Progress tracking**: Completed exercises are automatically tracked

## Ruff Configuration

Snakers uses Ruff for:
- Code formatting
- Style checking (PEP 8)
- Error detection
- Import sorting
- Modern Python practices

## Contributing

1. Fork the repository
2. Add new exercises in the appropriate topic directory
3. Follow the existing exercise format
4. Test your exercises
5. Submit a pull request

## Exercise Template

```python
"""
Exercise N: Title

Description of what the student will learn.

Tasks:
1. Task description
2. Another task

Hints:
- Helpful hint
- Another hint
"""

# TODO: Implementation task

def example_function():
    # TODO: Implement this function
    pass

if __name__ == "__main__":
    # Test code here
    pass
```

Happy coding! 🐍✨
