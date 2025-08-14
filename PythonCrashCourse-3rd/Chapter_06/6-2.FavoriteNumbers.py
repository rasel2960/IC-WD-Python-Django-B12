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
for name, number in favorite_numbers.items():
    print(f"Hey {name.title()}, your favourite number is {number}.")
print("\n")

print()

# For even more fun, poll a few friends and get some actual data for your program.
for name, number in favorite_numbers.items():
    num = float(input(f"Hello, {name.title()}! What is your favorite number? "))
    if num.is_integer():
        num = int(num)
    favorite_numbers[name] = num
    print(f"Thanks, {name.title()}! Your favorite number is now {number}")
print()
