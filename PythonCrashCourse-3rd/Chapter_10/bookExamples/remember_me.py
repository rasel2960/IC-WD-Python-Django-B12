# Saving and Reading User-Generated Data

import json
from pathlib import Path

username = input("What is your name? ")

path = Path('text_files/username.json')
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")
