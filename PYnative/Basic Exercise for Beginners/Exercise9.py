"""
Exercise 9: Check Palindrome Number
Write a Python code to check if the given number is a palindrome.
A palindrome number reads the same forwards and backward.
For example, 545 is a palindrome number.

Expected Output:
original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number

- Hint

Approach 1:
    Take the input number.
    Convert the number to a string.
    Reverse the string.
    Compare the original string with the reversed string.
    Return True if they are the same, False otherwise.

Approach 2:
    Reverse the given number using while loop and save it in a different variable.
    Use the if condition to check if the original and reverse numbers are identical. If yes, return True.
"""

# Approach 1

def check_palindrome(number):
    reversed_number = number[::-1]
    if number == reversed_number:
        print(f"Original number : {number}")
        print(f"Yes. Given number is palindrome number.")
    else:
        print(f"Original number : {number}")
        print(f"No. Given number is not palindrome number.")

number = input("Enter your number: ")
check_palindrome(number)

# Approach 2

def check_palindrome2(number):
    reversed_number = ""
    i = len(number) - 1
    while i >= 0:
        reversed_number += number[i]
        i -= 1

    if number == reversed_number:
        print(f"Original number : {number}")
        print(f"Yes. Given number is palindrome number.")
    else:
        print(f"Original number : {number}")
        print(f"No. Given number is not palindrome number.")

check_palindrome2(number)


