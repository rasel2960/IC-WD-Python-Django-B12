# from pathlib import Path
# import json
#
# path = Path('text_files/username.json')
#
# if path.exists():
#     contents = path.read_text(encoding='utf-8')
#     username = json.loads(contents)
#     print(f"Welcome back, {username}!")
# else:
#     username = input('Enter your name: ')
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")

# # Refactoring the above code
# from pathlib import Path
# import json
#
# def greet_user():
#     """Gree the user by name."""
#     path = Path('text_files/username.json')
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}!")
#     else:
#         username = input('Enter your name: ')
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")
# greet_user()


## More Refactoring
# from pathlib import Path
# import json
#
# def get_stored_username(path):
#     """Get stored username if available."""
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         return username
#     else:
#         return None
#
# def greet_user():
#     """Greet the user by name."""
#     path = Path('text_files/username.json')
#     username = get_stored_username(path)
#     if username:
#         print(f"Welcome back, {username.title()}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username.title()}!")
# greet_user()

### More Refactoring
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('text_files/usernames.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username.title()}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username.title()}!")
greet_user()