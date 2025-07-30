# 4-6. Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers = list(range(1,21,2))
print(odd_numbers)
for number in odd_numbers:
    print(number)
print("\n")
# 4-7. Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
multiple_numbers = []
for number in range(3,31):
    multiple_numbers.append(number * 3)
    print(number)
