# Snakers 🐍

Interactive Python exercises with Ruff linting - Learn Python by fixing and completing code!

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd snakers

# Install dependencies
pip install -e .
```

## Usage

### Run the next exercise
```bash
python snakers.py run
```

### Run a specific exercise
```bash
python snakers.py run 01_variables
```

### Watch mode (auto-check on file changes)
```bash
python snakers.py watch
```

### List all exercises
```bash
python snakers.py list
```

### Reset progress
```bash
python snakers.py reset
```

## Exercise Structure

Exercises are organized in the `exercises/` directory by topic:

- `01_basics/` - Variables, types, basic operations
- `02_functions/` - Function definitions, parameters, returns
- `03_data_structures/` - Lists, dictionaries, sets
- `04_classes/` - Object-oriented programming
- `05_modules/` - Imports, packages, modules

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
