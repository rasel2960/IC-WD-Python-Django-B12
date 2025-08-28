"""
3-7. Shrinking guest List:
You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests.
- Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner
- Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
- Print a message to each of the two people still on your list, letting them know they're still invited.
- Use del to remove the last two names from your list, so you have an empty list. Print your list to show that you have no guests.
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

print(f"Unfortunately, my new dinner table won't arrive in time for the dinner, and I have space for only two guests. So I have to remove some guests from the list.")
popped_guest_list = guest_list.pop()
print(f"Sorry! {popped_guest_list.title()}, Unfortunately, dinner invitation cancelled.")
popped_guest_list = guest_list.pop()
print(f"Sorry! {popped_guest_list.title()}, Unfortunately, dinner invitation cancelled.")
popped_guest_list = guest_list.pop()
print(f"Sorry! {popped_guest_list.title()}, Unfortunately, dinner invitation cancelled.")
popped_guest_list = guest_list.pop()
print(f"Sorry! {popped_guest_list.title()}, Unfortunately, dinner invitation cancelled.")
print(f"Dear {guest_list[0].title()} vai, I would like to invite you to dinner at my home.")
print(f"{guest_list[1].title()}, Please join the dinner at my home.")
del guest_list[0:]
print(guest_list)
