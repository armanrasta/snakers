"""
Exercise 16.3: Version Control with Git

Learn essential Git commands and workflows for Python projects.

Tasks:
1. Complete the functions for Git operations
2. Learn common Git workflows and best practices
3. Practice with branching, merging, and collaboration

Topics covered:
- Basic Git commands
- Branching and merging
- Remote repositories
- Collaborative workflows
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

def git_init(directory: Optional[Path] = None) -> Tuple[bool, str]:
    """
    Initialize a Git repository.
    
    Args:
        directory: Directory to initialize (default: current directory)
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Change to the specified directory if provided
    # TODO: Run git init command
    # TODO: Return success/failure and message
    pass

def git_status() -> Tuple[bool, str]:
    """
    Get the status of the Git repository.
    
    Returns:
        Tuple of (success, status_output)
    """
    # TODO: Run git status command
    # TODO: Return success/failure and output
    pass

def git_add(files: List[str]) -> Tuple[bool, str]:
    """
    Add files to the Git staging area.
    
    Args:
        files: List of files to add
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Run git add command for each file
    # TODO: Return success/failure and message
    pass

def git_commit(message: str) -> Tuple[bool, str]:
    """
    Commit changes to the Git repository.
    
    Args:
        message: Commit message
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Run git commit command with the message
    # TODO: Return success/failure and message
    pass

def git_branch(branch_name: Optional[str] = None) -> Tuple[bool, str]:
    """
    List branches or create a new branch.
    
    Args:
        branch_name: Name of the branch to create (None to list branches)
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: If branch_name is None, list branches
    # TODO: Otherwise, create a new branch
    # TODO: Return success/failure and message
    pass

def git_checkout(branch_name: str) -> Tuple[bool, str]:
    """
    Switch to a different branch.
    
    Args:
        branch_name: Name of the branch to switch to
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Run git checkout command
    # TODO: Return success/failure and message
    pass

def git_merge(branch_name: str) -> Tuple[bool, str]:
    """
    Merge a branch into the current branch.
    
    Args:
        branch_name: Name of the branch to merge
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Run git merge command
    # TODO: Return success/failure and message
    pass

def git_remote_add(name: str, url: str) -> Tuple[bool, str]:
    """
    Add a remote repository.
    
    Args:
        name: Name of the remote
        url: URL of the remote repository
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Run git remote add command
    # TODO: Return success/failure and message
    pass

def git_push(remote: str, branch: str) -> Tuple[bool, str]:
    """
    Push changes to a remote repository.
    
    Args:
        remote: Name of the remote
        branch: Name of the branch to push
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Run git push command
    # TODO: Return success/failure and message
    pass

def git_pull(remote: str, branch: str) -> Tuple[bool, str]:
    """
    Pull changes from a remote repository.
    
    Args:
        remote: Name of the remote
        branch: Name of the branch to pull
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Run git pull command
    # TODO: Return success/failure and message
    pass

def create_gitignore(directory: Optional[Path] = None) -> Tuple[bool, str]:
    """
    Create a .gitignore file for Python projects.
    
    Args:
        directory: Directory to create the file in (default: current directory)
        
    Returns:
        Tuple of (success, message)
    """
    # TODO: Create a .gitignore file with common Python entries
    # TODO: Return success/failure and message
    pass

class GitWorkflow:
    """A class to manage Git workflows."""
    
    def __init__(self, repo_path: Optional[Path] = None):
        """
        Initialize the Git workflow manager.
        
        Args:
            repo_path: Path to the Git repository
        """
        self.repo_path = repo_path or Path.cwd()
        # TODO: Check if this is a Git repository
    
    def feature_branch_workflow(self, feature_name: str) -> List[Tuple[bool, str]]:
        """
        Execute a feature branch workflow.
        
        Args:
            feature_name: Name of the feature
            
        Returns:
            List of (success, message) tuples for each step
        """
        # TODO: Create a feature branch
        # TODO: Make changes and commit
        # TODO: Merge back to main branch
        # TODO: Return results of each operation
        pass
    
    def get_commit_history(self, count: int = 10) -> List[Dict[str, str]]:
        """
        Get the commit history.
        
        Args:
            count: Number of commits to retrieve
            
        Returns:
            List of dictionaries with commit information
        """
        # TODO: Run git log command
        # TODO: Parse the output into a structured format
        # TODO: Return the commit history
        pass
    
    def resolve_merge_conflict(self, file_path: str, content: str) -> Tuple[bool, str]:
        """
        Resolve a merge conflict in a file.
        
        Args:
            file_path: Path to the conflicted file
            content: New content to resolve the conflict
            
        Returns:
            Tuple of (success, message)
        """
        # TODO: Write the new content to the file
        # TODO: Add the file to staging
        # TODO: Continue the merge
        # TODO: Return success/failure and message
        pass

if __name__ == "__main__":
    # Example usage
    print("Git Version Control Tool")
    print("----------------------")
    
    # Initialize repository if requested
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        directory = Path(sys.argv[2]) if len(sys.argv) > 2 else None
        success, message = git_init(directory)
        print(message)
        
        # Create .gitignore
        success, message = create_gitignore(directory)
        print(message)
    
    # Show status if requested
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        success, output = git_status()
        print(output)
    
    # Create a feature branch workflow if requested
    if len(sys.argv) > 1 and sys.argv[1] == "feature":
        feature_name = sys.argv[2] if len(sys.argv) > 2 else "new-feature"
        workflow = GitWorkflow()
        results = workflow.feature_branch_workflow(feature_name)
        
        print("\nFeature Branch Workflow:")
        for success, message in results:
            status = "✓" if success else "✗"
            print(f"{status} {message}")
    
    # Show commit history if requested
    if len(sys.argv) > 1 and sys.argv[1] == "history":
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        workflow = GitWorkflow()
        commits = workflow.get_commit_history(count)
        
        print(f"\nLast {count} commits:")
        for commit in commits:
            print(f"Commit: {commit.get('hash')}")
            print(f"Author: {commit.get('author')}")
            print(f"Date: {commit.get('date')}")
            print(f"Message: {commit.get('message')}")
            print()
