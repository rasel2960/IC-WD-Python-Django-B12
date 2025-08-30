"""
Exercise 7: Find the number of occurrences of a substring in a string
Write a Python code to find how often the substring “Emma” appears in the given string.

Given:
str_x = "Emma is good developer. Emma is a writer"

Expected Output:
Emma appeared 2 times

- Hint
Use string method count().
"""

def find_occurrences(full_string, sub_string):
    result = full_string.count(sub_string)
    return result

str_x = "Emma is good developer. Emma is a writer"
str_y = "Emma"

print(f"{str_y} appeared {find_occurrences(str_x, str_y)} times")
