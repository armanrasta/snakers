# Version Control with Git

Learn essential Git commands and workflows for Python projects.

## Exercise: Git Basics for Python Projects

### Part 1: Setting Up a Git Repository

```bash
# Initialize a new repository
mkdir my-python-project
cd my-python-project
git init

# Configure your identity
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Part 2: Creating a Python Project Structure

Create a basic project structure:

```bash
# Create directories and files
mkdir my_package
touch my_package/__init__.py
touch my_package/main.py
touch README.md
touch requirements.txt
touch .gitignore
```

Add this to your `.gitignore` file:

```
# Virtual environment
venv/
env/
.env/

# Python cache files
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Distribution / packaging
dist/
build/
*.egg-info/

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
coverage.xml
*.cover

# IDE specific files
.idea/
.vscode/
*.swp
*.swo
```

### Part 3: Basic Git Workflow

```bash
# Check status
git status

# Add files
git add my_package/__init__.py my_package/main.py

# Commit
git commit -m "Initial commit of package structure"

# Add more files
git add README.md .gitignore requirements.txt
git commit -m "Add project configuration files"
```

### Part 4: Branches and Merging

```bash
# Create a feature branch
git branch feature/add-logger
git checkout feature/add-logger
# OR in one command:
# git checkout -b feature/add-logger

# Make changes
echo "# Add logging functionality" >> my_package/logger.py

# Add and commit changes
git add my_package/logger.py
git commit -m "Add logger module"

# Switch back to main branch
git checkout main

# Merge feature branch
git merge feature/add-logger
```

### Part 5: Working with Remotes

```bash
# Add a remote repository (replace with your actual repository URL)
git remote add origin https://github.com/yourusername/my-python-project.git

# Push to remote
git push -u origin main

# Clone an existing repository
git clone https://github.com/someuser/some-python-project.git
```

### Part 6: Collaborative Workflows

```bash
# Pull latest changes
git pull

# Fetch changes without merging
git fetch
git diff origin/main

# Create a pull request (through GitHub/GitLab/etc.)
# 1. Push your branch
git push origin feature/my-new-feature

# 2. Open a pull request through the web interface
```

## Questions to Answer

1. Why is version control essential for Python projects?
2. What files should typically be included in a `.gitignore` file for Python projects?
3. What is the difference between `git fetch` and `git pull`?
4. Explain the purpose of branches in a development workflow.
5. What is a "merge conflict" and how would you resolve one?

## Challenge

Create a GitHub repository for a simple Python package with:
1. Proper directory structure
2. A README.md with installation and usage instructions
3. A proper .gitignore file
4. At least two branches (main and a feature branch)
5. A pull request that merges your feature into main
