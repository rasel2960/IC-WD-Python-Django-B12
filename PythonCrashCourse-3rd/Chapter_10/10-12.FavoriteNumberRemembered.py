"""
10-12. Favorite Number Remembered: 
Combine the two programs you wrote in Exercise 10-11 into one file. 
If the number is already stored, report the favorite number to the user. 
If not, prompt for the user’s favorite number and store it in a file. 
Run the program twice to see that it works.
"""
from pathlib import Path
import json

def get_stored_fav_number(path):
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        fav_number = json.loads(contents)
        return fav_number
    else:
        return None

def get_fav_number(path):
    fav_number = input("What is your favorite number? ")
    contents = json.dumps(fav_number)
    path.write_text(contents, encoding='utf-8')
    return fav_number

def show_fav_number():
    path = Path('files/favorite_number.json')
    fav_number = get_stored_fav_number(path)
    if fav_number:
        print(f"I know your favorite number! It's {fav_number}.")
    else:
        fav_number = get_fav_number(path)
        print(f"I know your favorite number! It's {fav_number}.")

show_fav_number()
