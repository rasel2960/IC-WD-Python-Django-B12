"""
10-5. Guest Book:
Write a while loop that prompts users for their name.
Collect all the names that are entered, and then write these names to a file called guest_book.txt.
Make sure each entry appears on a new line in the file.
"""

from pathlib import Path
file_path = Path('files/guest_book.txt')
names = []

while True:
    message = "Please enter your name\n"
    message += "or enter 'q' to quit: "
    name = input(message)
    if name.lower() == 'q':
        break
    names.append(name)

names = "\n".join(names)

file_path.write_text(names.title())