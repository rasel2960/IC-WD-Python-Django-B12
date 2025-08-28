"""3-9. Dinner Guests:
Working with one of the programs from Exercises 3-4 through 3-7 (pages 41-42),
use len() to print a message indicating the number of people you are inviting to dinner.
"""

guest_list = ['naim', 'Salauddin', 'Fahmida']
print(f"Dear {guest_list[0].title()} vai, I would like to invite you to dinner at my home.")
print(f"{guest_list[1].title()}, Please join the dinner at my home.")
print(f"Hey {guest_list[2].title()} madam, you are invited to dinner at my home.")

print(f"\nI am inviting {len(guest_list)} people to dinner.")

