"""
10-14: Verify User
The final listing for remember_me.py assumes either that the user has already entered their username
or that the program is running for the first time.
We should modify it in case the current user is not the person who last used the program.
Before printing a welcome back message in greet_user(), ask the user if this is the correct username.
If it's not, call get_new_username() to get the correct username.
"""

from pathlib import Path
import json

def get_stored_username(path):
    """Retrieve the stored username from the given path if it exists."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Ask the user to enter their username and store it for later use"""
    username = input("What's your username? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user."""
    path = Path('files/username.json')
    username = get_stored_username(path)
    if username:
        verify_user = input(f"Are you {username}? (y/n) ")
        if verify_user.lower() == "y":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"Thank's {username}! We'll remember your info when you return.")
    else:
        username = get_new_username(path)
        print(f"Thank's {username}! We'll remember your info when you return.")

greet_user()
