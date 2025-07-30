# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python Program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# number1 = 200
# number2 = 30
# multiply_number = number1 * number2
# sum_number = number1 + number2

# Function for Restrict Input to Digits Only (0-9)
# def get_valid_number(prompt):
#     while True:
#         user_input = input(prompt)
#         if user_input.isdigit():
#             return int(user_input)
#         else:
#             print("X Invalid Digits. lease enter a valid number (0-9 only).")

def get_valid_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("X Invalid input. Please enter a valid number.")

def calculate_sum_product(number1, number2):
    multiply_number = number1 * number2
    sum_number = number1 + number2
    if multiply_number <= 1000:
        print(multiply_number)
        return multiply_number
    else:
        print(sum_number)
        return sum_number

calculate_sum_product(get_valid_number("Enter first number: "), get_valid_number("Enter second number: "))