"""
9-13. Dice:
Make a class Die with one attribute called sides, which has a default value of 6.
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

# Making a 6-sided die and showing the results of 10 rolls
die6 = Die()
results = []
for roll_num in range(10):
    result = die6.roll_die()
    results.append(result)
print(f"10 rolls of a 6-sided die:\n{results}")


# Making a 10-sided die and showing the results of 10 rolls
die6 = Die(sides=10)
results = []
for roll_num in range(10):
    result = die6.roll_die()
    results.append(result)
print(f"\n10 rolls of a 10-sided die:\n{results}")

# Making a 20-sided die and showing the results of 10 rolls
die6 = Die(sides=20)
results = []
for roll_num in range(10):
    result = die6.roll_die()
    results.append(result)
print(f"\n10 rolls of a 20-sided die:\n{results}")
