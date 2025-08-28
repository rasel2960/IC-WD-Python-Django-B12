"""
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize.
"""

from random import  choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []

print("Let's see what the winning tickets are ....")

while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    if pulled_item not in winning_ticket:
        print(f"We pulled  {pulled_item}!")
        winning_ticket.append(pulled_item)
print(f"\nThe final winning tickets is: {winning_ticket}")
