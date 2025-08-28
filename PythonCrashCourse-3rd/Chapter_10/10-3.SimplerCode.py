"""
10-3. Simpler Code:
The program file_reader.py in this section uses a temporary variable, lines, to show how splitlines() works.
You can skip the temporary variable and loop directly over the list that splitlines() returns:
for line in contents.splitlines():
Remove the temporary variable from each of the programs in this section, to make them more concise.
"""

from pathlib import Path
file = Path('learning_python.txt')
file_contents = file.read_text()

# Original contents
for line in file_contents.splitlines():
    print(line)

# Modified contents
for line in file_contents.splitlines():
    print(line.replace('Python', 'C'))