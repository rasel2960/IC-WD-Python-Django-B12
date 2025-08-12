"""
5-1. Conditonal Tests:
Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each
test. Your code should look someting like this:
---------------------------------------------------------------
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
----------------------------------------------------------------

- Look closely at your results, and make sure you understand why each line evaluates to True or False.
- Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
"""

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

cars = ['subaru', 'audi', 'toyota', 'honda', 'ford']
print("\n Is 'subaru' in cars? I predict True.")
print(cars[0] == 'subaru')

print("\n Is 'Audi' in cars? I predict False.")
print(cars[1] == 'Audi')

print(f"\n Is cars[2] == 'Toyota'? I predict False.")
print(cars[2].lower() == 'toyota')

print(f"\n Is cars[3] == 'honda'? I predict True.")
print(cars[3] == 'honda')

print(f"\n Is cars[4] == 'Ferrari'? I predict False.")
print(cars[4] == 'Ferrari')

# 5-2. More Conditional Tests: You don't have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests
# and add them to ConditionalTests.py. Have at least one True and one False for each of the following:
# - Tests for equality and inequality with strings
# - Tests using the lower() method
# - Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
# - Tests using the and keyword and or keyword
# - Test whether an item is in a list
# - Test whether an item is not in a list
print("\n")
fname = 'Rasel'
lname = 'Ahmed'
print(fname == lname)

print("\n")
print(fname != lname)

print("\n")
print(fname.lower() == 'rasel')
print(lname.title() == 'Ahmed')

print("\n")
age0 = 25
age1 = 30
print(f"Is age0 >= age1? I predict False. \nResult: {age0 >= age1}")
print(f"Is age0 >= 18 or age1 < 30? I predict True. \nResult: {age0 >= 18 or age1 < 30}")

print("\n")
numbers = [1, 2, 3, 4, 5]
print(f"Is 3 in numbers? I predict True. \nResult: {3 in numbers}")

print("\n")
print(f"Is 5 not in numbers? I predict False. \nResult: {5 not in numbers}")