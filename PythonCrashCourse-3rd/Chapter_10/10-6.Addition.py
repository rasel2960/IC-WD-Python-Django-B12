"""
10-6. Addition:
One common problem when prompting for numerical input occurs when people provide text instead of numbers.
When you try to convert the input to an int, you’ll get a ValueError.
Write a program that prompts for two numbers.
Add them together and print the result.
Catch the ValueError if either input value is not a number, and print a friendly error message.
Test your program by entering two numbers and then by entering some text instead of a number.
"""

print("Enter two numbers & I'll add them.\n")
first_number = input("First Number : ")
second_number = input("Second Number : ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Incorrect number. Please try again.")
else:
    print("The answer is: ", answer)
