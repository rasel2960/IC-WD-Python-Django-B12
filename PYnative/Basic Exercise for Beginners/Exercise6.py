"""
Exercise 6: Display numbers divisible by 5
Write a Python code to display numbers from a list divisible by 5

Expected Output:
Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55

- Hint
Iterate through each number in the list using a for loop.
For each number, use the modulo operator (%) to find the remainder when divided by 5.
If the remainder is 0, it means the number is divisible by 5. In that case, print the number.
"""

def divisible_by_5(numbers):
    for number in numbers:
        if number % 5 == 0:
            print(number)

number_list = [10, 20, 33, 46, 55]
print(f"Given List is : {number_list}\nDivisible by 5")
divisible_by_5(number_list)