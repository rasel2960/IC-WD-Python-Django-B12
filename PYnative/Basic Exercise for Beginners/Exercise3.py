"""
Exercise 3: Print characters present at an even index number
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

Expected Output:
                Original String is  PYnative
                Printing only even index chars
                P
                n
                t
                v
"""

# user_input = input("Enter a string from the user: ")
user_input = 'PYnative'

print(f"Original String is  {user_input}")
print("Printing only even index chars")

for i in range(0, len(user_input), 2):
    char = user_input[i]
    print(char)
