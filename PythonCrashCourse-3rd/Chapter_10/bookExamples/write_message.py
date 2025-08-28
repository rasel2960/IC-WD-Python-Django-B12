from pathlib import Path
file_path = Path('text_files/programming.txt')

# Writing to a file
file_path.write_text("I love programming.")

# Writing multiple lines to a file
file_contents = ("I love programming.\n"
                 "I love creating new games.\n"
                 "I love learning new programming languages.\n")
file_path.write_text(file_contents)