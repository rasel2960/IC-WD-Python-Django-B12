"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

Given 1:                Given 2:
number1 = 20            number1 = 40
number2 = 30            number2 = 30

Expected Output:        Expected Output:
The result is 600       The result is 70

Show Hint
- Create a function that takes two numbers as parameters.
- Inside the function:
    - Multiply these two numbers.
    - Store their product in a variable.
    - Check if the product is greater than 1000 using an if condition.
        - If the product is greater than 1000, return the product.
        - Otherwise (in the else block):
            - Calculate the sum of the two numbers.
            - Return the sum.
"""

def show_calculation(num1, num2):
    result = num1 * num2
    if result > 1000:
        result = num1 + num2
        return result
    else:
        return result

result = show_calculation(20, 30)
print(f"The result is {result}")

result = show_calculation(40, 30)
print(f"The result is {result}")