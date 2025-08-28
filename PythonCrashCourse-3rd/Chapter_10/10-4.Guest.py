"""
10-4. Guest:
Write a program that prompts the user for their name.
When they respond, write their name to a file called guest.txt.
"""

from pathlib import Path

file_path = Path('files/guest.txt')

name = input("What is your name? ")
file_path.write_text(f"My Name is : {name.title()}")