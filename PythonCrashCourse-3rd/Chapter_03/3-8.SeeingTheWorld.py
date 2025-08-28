"""
3-8. Seeing the World:
Think of at least five places in the world you'd like to visit.
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


