# 6-2. Favorite Numbers:
# Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favorite_numbers = {
    'alice': 7,
    'bob': 3,
    'charlie': 5,
    'dave': 9,
    'eve': 2,
}

# 6-10. Favorite Numbers:
# Modify your program from Exercise 6-2 (page 98)
# so each person can have more than one favorite number.
# Then print each person’s name along with their favorite numbers.

favorite_numbers = {
    'alice': [7, 14],
    'bob': [3, 6],
    'charlie': [5, 10],
    'dave': [9, 18],
    'eve': [2, 4],
}

for name, numbers in favorite_numbers.items():
    print(f"\nHey {name.title()}, your favourite number is: ")
    for number in numbers:
        print(f"\t- {number}")
print("\n")

# For even more fun, poll a few friends and get some actual data for your program.

