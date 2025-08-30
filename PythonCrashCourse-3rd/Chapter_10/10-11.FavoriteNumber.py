"""
10-11. Favorite Number:
Write a program that prompts for the user’s favorite number.
Use json.dumps() to store this number in a file.
Write a separate program that reads in this value and prints the message “I know your favorite number! It’s _____.”
"""


from pathlib import Path
import json

def store_fav_number():
    path = Path('files/favorite_number.json')
    fav_number = input('Enter your favorite number: ')
    content = json.dumps(fav_number)
    path.write_text(content, encoding='utf-8')
    return fav_number

store_fav_number()

def load_fav_number():
    path = Path('files/favorite_number.json')
    content = path.read_text(encoding='utf-8')
    fav_number = json.loads(content)
    print(f"I know your favorite number. It's {fav_number}")
load_fav_number()