"""
3-6. More Guests:
You just found a bigger table, so now more space is available.
Think of three more guests to invite to dinner.
- Start with your program from Exercise 3-4 or 3-5.
- Add a print() call to the end of your program, informing people that you found a bigger table.
- Use insert() to add one new guest to the beginning of your list.
- Use insert() to add one new guest to the middle of your list.
- Use append() to add one new guest to the end of your list.
- Print a new set of invitation messages, one for each person in your list.
"""

''' ----- Starts 3.4 ----- '''
guest_list = ['naim', 'Salauddin', 'Fahmida']
print(f"Dear {guest_list[0].title()} vai, I would like to invite you to dinner at my home.")
print(f"{guest_list[1].title()}, Please join the dinner at my home.")
print(f"Hey {guest_list[2].title()} madam, you are invited to dinner at my home.")
''' ----- Ends 3.4 ----- '''


''' ----- Starts 3.5 ----- '''
print(f"Unfortunately, {guest_list[2].title()} can't make it to the dinner. So, I'm going to invite another of my friend instead.")
guest_list[2] = 'shamim'
print(f"Dear {guest_list[0].title()} vai, I would like to invite you to dinner at my home.")
print(f"{guest_list[1].title()}, Please join the dinner at my home.")
print(f"Hey {guest_list[2].title()}, you are invited to dinner at my home.")
''' ----- Ends 3.5 ----- '''

''' ----- Starts 3.6 ----- '''
guest_list.insert(0, 'jion')
guest_list.insert(3, 'zadid')
guest_list.append('asif')

print(f"Dear {guest_list[0].title()} vai, I would like to invite you to dinner at my home.")
print(f"{guest_list[1].title()}, Please join the dinner at my home.")
print(f"Hey {guest_list[2].title()}, you are invited to dinner at my home.")
print(f"Dear {guest_list[3].title()}, I would like to invite you to dinner at my home.")
print(f"{guest_list[4].title()}, Please join the dinner at my home.")
print(f"Hey {guest_list[5].title()}, you are invited to dinner at my home.")
''' ----- Ends 3.6 ----- '''
