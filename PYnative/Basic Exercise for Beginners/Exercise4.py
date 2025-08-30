"""
Exercise 4: Remove first n characters from a string
Write a Python code to remove characters from a string from 0 to n and return a new string.

Given:
def remove_chars(word, n):
    # write your code

print("Removing characters from a string")
print(remove_chars("pynative", 4))
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2))
# output 'native'

Note: n must be less than the length of the string.

Hint -
Use string slicing to get a substring.
Think about how you can use the slicing notation [:] along with the value of n to select the portion of the string after the first n characters.
"""

def remove_chars(word, n):
    print("Original string:", word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
