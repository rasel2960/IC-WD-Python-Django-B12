# 7-3. Multiples of Ten:
# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = input("Please enter a number and I'll tell you if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"\nOh no! The number {number} is not a multiple of 10.")