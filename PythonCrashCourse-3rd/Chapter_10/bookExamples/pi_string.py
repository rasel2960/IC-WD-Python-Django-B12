# Working with a File's Contents

from pathlib import Path

# path = Path('text_files/pi_digits.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# pi_string = ''
#
# for line in lines:
#     pi_string += line
#
# print(pi_string)
# print(len(pi_string))

# Large Files: One Million Digits

path = Path('text_files/pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}....")
print(len(pi_string))
