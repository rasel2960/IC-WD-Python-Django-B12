"""
3-10. Every Function:
Think of things you could store in a list.
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like.
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
"""

countries = ['Bangladesh', 'India', 'Pakistan', 'Nepal', 'Bhutan']

print(f"\n Original Order:")
print(countries)  # Original list

print(f"\nAlphabetical Order:")
print(sorted(countries))  # Sorted list in alphabetical order

print(f"\nOriginal Order Again:")
print(countries)  # Original list again

print(f"\nReverse Alphabetical Order:")
print(sorted(countries, reverse=True))  # Sorted list in reverse alphabetical order

print(f"\nOriginal Order Again:")
print(countries)  # Original list again

print(f"\nReversed Order:")
countries.reverse()  # Reverse the list
print(countries)  # Print the reversed list

print(f"\noriginal Order Again:")
print(countries)

print(f"\nAlphabetical Order:")
countries.sort()
print(countries)   # Sort the list in alphabetical order

print(f"\nalphabetical Order in Reverse:")
countries.sort(reverse=True)  # Sort the list in reverse alphabetical order
print(countries)

