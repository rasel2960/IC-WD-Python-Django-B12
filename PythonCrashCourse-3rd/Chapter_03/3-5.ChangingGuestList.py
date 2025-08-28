"""
3-5. Changing Guest List:
You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations.
You'll have to think of someone else to invite.
- Start with your program from Exercise 3-4.
- Add a print statement at the end of your program stating the name of the guest who can't make it.
- Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
- Print a second set of invitation messages, one for each person who is still in your list.
"""

''' ----- Starts 3.4 ----- '''
guest_list = ['naim', 'Salauddin', 'Fahmida']
print(f"Dear {guest_list[0].title()} vai, I would like to invite you to dinner at my home.")
print(f"{guest_list[1].title()}, Please join the dinner at my home.")
print(f"Hey {guest_list[2].title()} madam, you are invited to dinner at my home.")
''' ----- Ends 3.4 ----- '''

print(f"Unfortunately, {guest_list[2].title()} can't make it to the dinner. So, I'm going to invite another of my friend instead.")
guest_list[2] = 'shamim'
print(f"Dear {guest_list[0].title()} vai, I would like to invite you to dinner at my home.")
print(f"{guest_list[1].title()}, Please join the dinner at my home.")
print(f"Hey {guest_list[2].title()}, you are invited to dinner at my home.")
