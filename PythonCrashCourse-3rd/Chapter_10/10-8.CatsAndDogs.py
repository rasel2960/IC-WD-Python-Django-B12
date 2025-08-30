"""
10-8. Cats and Dogs:
Make two files, cats.txt and dogs.txt.
Store at least three names of cats in the first file and three names of dogs in the second file.
Write a program that tries to read these files and print the contents of the file to the screen.
Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing.
Move one of the files to a different location on your system, and make sure the code in the except block executes properly.
"""

from pathlib import Path

# # Without Changing file locations
# file_names = ['cats.txt', 'dogs.txt']

# Code  changed for another location

folder = Path('files')
file_names = ['cats.txt', 'dogs.txt']

for file_name in file_names:
    path = folder / file_name
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        print(f"\nReading files from: {file_name}\n{contents}")

