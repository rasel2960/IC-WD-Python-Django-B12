"""
10-5. Guest Book:
Write a while loop that prompts users for their name.
Collect all the names that are entered, and then write these names to a file called guest_book.txt.
Make sure each entry appears on a new line in the file.
"""

from pathlib import Path
file_path = Path('files/guest_book.txt')

message = "\nPlease enter your name\n"
message += "or enter 'q' to quit: "

guest_names = []
while True:
    name = input(message)
    if name.lower() == 'q':
        break
    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)

# Method 1
names = "\n".join(guest_names)
file_path.write_text(names.title())

# # Method 2
# file_string = ''
# for name in guest_names:
#     file_string += f"{name.title()}\n"
# file_path.write_text(file_string)

# # Method 3 with append mode
# with file_path.open('a') as file:
#     for name in guest_names:
#         file.write(f"{name.title()}\n")

