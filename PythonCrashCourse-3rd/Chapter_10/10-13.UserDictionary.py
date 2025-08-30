"""
10-13. User Dictionary:
The remember_me.py example only stores one piece of information, the username.
Expand this example by asking for two more pieces of information about the user, then store all the information you collect in a dictionary.
Write this dictionary to a file using json.dumps(), and read it back in using json.loads().
Print a summary showing exactly what your program remembers about the user.
"""

from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user infor if available"""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_user_info(path):
    """Get information from new user"""
    username = input("What's your name? ")
    age = input("How old are you? ")
    location = input("Where do you live? ")

    user_dict = {
        'username': username,
        'age': age,
        'location': location,
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    """Greet the user by name and state what we know about them"""
    path = Path('files/user_dict.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        if user_dict['location'].lower() == 'bangladesh':
            print(f"Your country is going to arrange National Election in the next year")
        else:
            print(f"I have a plan to visit your country one day")
        if int(user_dict['age']) >= 18:
            print("You are old enough to vote for 2025's National Election")
        else:
            print(f"Sorry! Your are not eligible for 2025's National Election")
    else:
        user_dict = get_new_user_info(path)
        print(f"We'll remember your info when you return: {user_dict['username']}")

greet_user()