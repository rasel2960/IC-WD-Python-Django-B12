# Greets a user whose name has already been stored

import json
from pathlib import Path

path = Path('text_files/username.json')
contents = path.read_text()
username = json.loads(contents)
print(f"Welcome back, {username}!")
