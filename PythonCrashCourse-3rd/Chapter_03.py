# Python Crash Course, 3rd Edition by Eric Matthes
# Chapter 2: Introducing Lists
# Try It Yourself
from traceback import print_tb
from wsgiref.util import guess_scheme

# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person's name by accessing each element in the list, one at a time.
names = ['monjur', 'najmul', 'dipol', 'zillur', 'mamun', 'zahid']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of printing each person's name, print a message to them. The text of each message should be the same, but each message should be personalized with the person's name.
print(f"My best friend's name is {names[0].title()}.")
print(f"One of my friends name is {names[1].upper()}.")
print(f"One of my friends name is {names[2].lower()}.")
print(f"One of my friends name is {names[3].capitalize()}.")
print(f"One of my friends name is {names[4]}.")
print(f"One of my friends name is {names[5]}.")

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle."
transportation = ['motorcycle', 'car', 'bicycle', 'bus', 'train']
print(f"I already have a Honda CB Trigeer {transportation[0].title()}.")
print(f"I would like to own a {transportation[1].title()}.")
print(f"In my college time I had a {transportation[2].title()} which was given by my Father.")
print(f"I don't like to travel by {transportation[3].title()} from my childhood. Hearing the name of {transportation[3].title()} makes me feel sick.")
print(f"Travelling by {transportation[4].title()} was a great experience for me. I came back to Tangail from Rajshahi by {transportation[4].title()} in 2009. It was a great experience for me.")

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
guest_list = ['naim', 'Salauddin', 'Fahmida']
print(f"Dear {guest_list[0].title()} vai, I would like to invite you to dinner at my home.")
print(f"{guest_list[1].title()}, Please join the dinner at my home.")
print(f"Hey {guest_list[2].title()} madam, you are invited to dinner at my home.")

# 3-5. Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
"""
- Start with your program from Exercise 3-4. Add a print statement at the end of your program stating the name of the guest who can't make it.
- Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
- Print a second set of invitation messages, one for each person who is still in your list.
"""
print(f"Unfortunately, {guest_list[2].title()} can't make it to the dinner. So, I'm going to invite another of my friend instead.")
guest_list[2] = 'shamim'
print(f"Dear {guest_list[0].title()} vai, I would like to invite you to dinner at my home.")
print(f"{guest_list[1].title()}, Please join the dinner at my home.")
print(f"Hey {guest_list[2].title()}, you are invited to dinner at my home.")


# 3-6. More Guests: You just found a bigger table, so now more space is avilable. Think of three more guests to invite to dinner.
"""
- Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
- Use insert() to add one new guest to the beginning of your list.
- Use insert() to add one new guest to the middle of your list.
- Use append() to add one new guest to the end of your list.
- Print a new set of invitation messages, one for each person in your list.
"""
guest_list.insert(0, 'jion')
guest_list.insert(3, 'zadid')
guest_list.append('asif')

print(f"Dear {guest_list[0].title()} vai, I would like to invite you to dinner at my home.")
print(f"{guest_list[1].title()}, Please join the dinner at my home.")
print(f"Hey {guest_list[2].title()}, you are invited to dinner at my home.")
print(f"Dear {guest_list[3].title()}, I would like to invite you to dinner at my home.")
print(f"{guest_list[4].title()}, Please join the dinner at my home.")
print(f"Hey {guest_list[5].title()}, you are invited to dinner at my home.")

# 3-7. Shrinking guest List: You just found out that your new dinner table won't arrive in time for the dinner, and you have space for only two guests.
"""
- Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner
- Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
- Print a message to each of the two people still on your list, letting them know they're still invited.
- Use del to remove the last two names from your list, so you have an empty list. Print your list to show that you have no guests.
"""
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

# 3-8. Seeing the World: Think of at least five places in the world you'd like to visit.
"""
- Store the locations in a list. Make sure the list is not in alphabetical order.
- Print your list in its original order. Don't worry about printing the list neatly, just print it as a raw Python list.
- Use sorted() to print your list in alphabetical order without modifying the actual list.
- Show that your list is still in its original order by printing it again.
- Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
- Show that your list is still in its original order by printing it again.
- Use reverse() to change the order of your list. Print the list to show that its order has changed.
- Use reverse() to change the order of your list again. Print the list to show that its order has changed back to the original.
- Use sort() to change your list so it's stored in alphabetical order. Print the list to show that its order has been changed.
- Use sort() to change your list so it's stored in reverse alphabetical order. Print the list to show that its order has changed.
"""
places = ['paris', 'new york', 'tokyo', 'london', 'sydney'] # 3-8.1
print(f"\nHere is the original list")
print(places)  # 3-8.2

print(f"\nHere is the sorted list in alphabetical order")
print(sorted(places)) # 3-8.3

print(f"\nHere is the original list again")
print(places)   # 3-8.4

print(f"\nHere is the sorted list in reverse alphabetical order")
print(sorted(places, reverse=True)) # 3-8.5

print(f"\nHere is the original list again")
print(places)   # 3-8.6

print(f"\nHere is the list in reverse order")
places.reverse() # 3-8.7
print(places)

print(f"\nHere is the list in reverse order again")
places.reverse() # 3-8.8
print(places)

print(f"\nHere is the Sorted list in alphabetical order")
places.sort() # 3-8.9
print(places)

print(f"\nHere is the Sorted list in reverse alphabetical order")
places.sort(reverse=True) # 3-8.10
print(places)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41-42), use len() to print a message indicating the number of people you are inviting to dinner.
print(f"\nI am inviting {len(guest_list)} people to dinner.")

# 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
countries = ['Bangladesh', 'India', 'Pakistan', 'Nepal', 'Bhutan']

print(f"\n Original Order:")
print(countries)  # Original list

print(f"\nAlphabetical Order:")
print(sorted(countries))  # Sorted list in alphabetical order

print(f"\nOriginal Order Again:")
print(countries)  # Original list again

print(f"\nReverse Alphabetical Order:")
print(sorted(countries, reverse=True))  # Sorted list in reverse alphabetical order

print(f"\nOriginal Order Again:")
print(countries)  # Original list again

print(f"\nReversed Order:")
countries.reverse()  # Reverse the list
print(countries)  # Print the reversed list

print(f"\noriginal Order Again:")
print(countries)

print(f"\nAlphabetical Order:")
countries.sort()
print(countries)   # Sort the list in alphabetical order

print(f"\nalphabetical Order in Reverse:")
countries.sort(reverse=True)  # Sort the list in reverse alphabetical order
print(countries)

