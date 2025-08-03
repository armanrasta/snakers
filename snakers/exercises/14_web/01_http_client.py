"""
Exercise 14.1: HTTP Clients and APIs

Learn about making HTTP requests and working with APIs.

Tasks:
1. Complete the functions below
2. Practice making HTTP requests
3. Work with JSON responses and error handling

Topics covered:
- HTTP GET and POST requests
- Working with JSON data
- Request parameters and headers
- Error handling
"""

import json
from typing import Dict, Any, List, Optional, Union
import urllib.request
import urllib.error
import urllib.parse

# For this exercise, we'll use a public test API: https://jsonplaceholder.typicode.com

def get_resource(url: str) -> Dict[str, Any]:
    """
    Make a GET request to fetch a resource.
    
    Args:
        url: URL to fetch
        
    Returns:
        Parsed JSON response as dictionary
        
    Raises:
        urllib.error.HTTPError: If HTTP request fails
    """
    # TODO: Make a GET request to the URL
    # TODO: Parse JSON response and return as dictionary
    # TODO: Handle HTTP errors properly
    pass

def get_all_posts() -> List[Dict[str, Any]]:
    """
    Fetch all posts from the API.
    
    Returns:
        List of post dictionaries
    """
    # TODO: Make a GET request to fetch all posts
    # TODO: Use the get_resource function
    pass

def get_post_by_id(post_id: int) -> Optional[Dict[str, Any]]:
    """
    Fetch a specific post by ID.
    
    Args:
        post_id: ID of the post to fetch
        
    Returns:
        Post dictionary or None if not found
    """
    # TODO: Make a GET request to fetch a specific post
    # TODO: Handle 404 errors (return None if not found)
    pass

def get_comments_for_post(post_id: int) -> List[Dict[str, Any]]:
    """
    Fetch all comments for a specific post.
    
    Args:
        post_id: ID of the post
        
    Returns:
        List of comment dictionaries
    """
    # TODO: Make a GET request to fetch comments for a post
    # TODO: Use query parameters to filter by post ID
    pass

def create_post(title: str, body: str, user_id: int) -> Dict[str, Any]:
    """
    Create a new post.
    
    Args:
        title: Post title
        body: Post body
        user_id: User ID
        
    Returns:
        Created post as dictionary
    """
    # TODO: Create a dictionary with post data
    # TODO: Make a POST request to create a new post
    # TODO: Set appropriate headers (Content-Type)
    pass

def search_posts(query: str) -> List[Dict[str, Any]]:
    """
    Search posts by title or body.
    
    Args:
        query: Search query
        
    Returns:
        List of matching post dictionaries
    """
    # TODO: Fetch all posts
    # TODO: Filter posts that contain the query in title or body
    # TODO: Return the filtered list
    pass

def download_and_save_user_data(user_id: int, filename: str) -> bool:
    """
    Download user data and save to a JSON file.
    
    Args:
        user_id: User ID to fetch
        filename: File to save the data to
        
    Returns:
        True if successful, False otherwise
    """
    # TODO: Fetch user data
    # TODO: Save the data to a JSON file
    # TODO: Return True if successful, False on error
    pass

if __name__ == "__main__":
    # Test the functions
    print("Fetching posts...")
    posts = get_all_posts()
    print(f"Fetched {len(posts)} posts")
    
    print("\nFetching post with ID 1...")
    post = get_post_by_id(1)
    if post:
        print(f"Post title: {post['title']}")
    
    print("\nFetching comments for post 1...")
    comments = get_comments_for_post(1)
    print(f"Found {len(comments)} comments")
    
    print("\nCreating a new post...")
    new_post = create_post(
        "Test Post",
        "This is a test post created during the Python exercise.",
        1
    )
    print(f"Created post with ID: {new_post['id']}")
    
    print("\nSearching for posts containing 'error'...")
    error_posts = search_posts("error")
    print(f"Found {len(error_posts)} posts matching the search")
    
    print("\nDownloading user data...")
    success = download_and_save_user_data(1, "user_data.json")
    if success:
        print("User data saved successfully")
    else:
        print("Failed to save user data")
