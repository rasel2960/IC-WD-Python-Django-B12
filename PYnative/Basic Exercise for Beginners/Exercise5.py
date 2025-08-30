"""
Exercise 5:
Check if the first and last numbers of a list are the same.
Write a code to return True if the list’s first and last numbers are the same.
If the numbers are different, return False.

Given:
numbers_x = [10, 20, 30, 40, 10]
# output True

numbers_y = [75, 65, 35, 75, 30]
# Output False

- Hint
Use list indexing.
Get the first element of the list.
Get the last element of the list.
Compare these two elements using the equality operator (==).
"""

def check_equal(num_list):
    if not num_list:
        return "Oh Sorry! There's nothing to check or the list is empty."
    return num_list[0] == num_list[-1]

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
numbers_z = []

print(check_equal(numbers_x))
print(check_equal(numbers_y))
print(check_equal(numbers_z))