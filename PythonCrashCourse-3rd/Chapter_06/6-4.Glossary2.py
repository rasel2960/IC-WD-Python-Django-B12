# 6-3. Glossary:
# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.•
# • Think of five programming words you’ve learned about in the previous
    #   chapters. Use these words as the keys in your glossary, and store their
    #   meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
    #   print the word followed by a colon and then its meaning, or print the word
    #   on one line and then print its meaning indented on a second line. Use the
    #   newline character (\n) to insert a blank line between each word-meaning
    #   pair in your output.

glossary = {
    'variable': 'A named location in memory used to store data.',
    'string': 'A sequence of characters enclosed in quotes.',
    'integer': 'A whole number without a fractional part.',
    'float': 'A number that has a decimal point, representing a real number.',
    'boolean': 'A data type that can be either True or False.',
}

# # Printing each word followed by a colon and then its meaning
# meaning = glossary['variable'].capitalize()
# print(f"{'variable'.title()}: {meaning}")
#
# meaning = glossary['string'].capitalize()
# print(f"{'string'.title()}: {meaning}")
#
# meaning = glossary['integer'].capitalize()
# print(f"{'integer'.title()}: {meaning}")
#
# meaning = glossary['float'].capitalize()
# print(f"{'float'.title()}: {meaning}")
#
# meaning = glossary['boolean'].capitalize()
# print(f"{'boolean'.title()}: {meaning}")
#
# meaning = glossary.get('loop', "No value assigned").capitalize()
# print(f"{'loop'.title()}: {meaning}")
#
# print()
# # Printing the word on one line and then print its meaning indented on a second line
# meaning = glossary['variable'].capitalize()
# print(f"{'variable'.title()}:\n\t{meaning}")
#
# meaning = glossary['string'].capitalize()
# print(f"{'string'.title()}:\n\t{meaning}")
#
# meaning = glossary['integer'].capitalize()
# print(f"{'integer'.title()}:\n\t{meaning}")
#
# meaning = glossary['float'].capitalize()
# print(f"{'float'.title()}:\n\t{meaning}")
#
# meaning = glossary['boolean'].capitalize()
# print(f"{'boolean'.title()}:\n\t{meaning}")
#
# meaning = glossary.get('loop', "No value assigned").capitalize()
# print(f"{'loop'.title()}:\n\t{meaning}")
#
# print()

"""
6-4. Glossary 2:
Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
"""

glossary['loop'] = 'A control structure that repeats a block of code multiple times.'
glossary.update({'list': 'An ordered collection of items that can be changed.'})

glossary_item = ['iteration', 'iterable', 'index', 'tuple', 'set', 'scope']
glossary_value = ['A single pass through a loop.', 'An object that can be iterated over.', 'An integer representing the position of an item in a sequence.', 'An immutable ordered collection of items.', 'An unordered collection of unique items.', 'The context in which a variable is defined.']

for item, value in enumerate(glossary_item):
    glossary[value] = glossary_value[item]

print()


# Printing each word followed by a colon and then its meaning
for key, value in glossary.items():
    print(f"{key.title()}: {value}")
print()

# Printing the word on one line and then print its meaning indented on a second line
for key, value in glossary.items():
    print(f"{key.title()}:")
    print(f"\t{value}\n")
