# 4-10. Slices: Use one of the programs your wrote in this chapter, and several lines to the end of the program that do the following:
# - Print the message 'The first three items in the list are:'. Then use a slice to print the first three items from that program's list.
# - Print the message 'Three items from the middle of the list are:'. then use a slice to tprint three items from the middle of the list.
# - Print the message 'the last three items in the list are:'. Then use a slice to print the last three items from the list.
books = ['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Catcher in the Rye']

print(f"The first three items in the list are:")
print(books[0:3])

print(f"Three items from the middle of the list are:")
middle_index = len(books) // 2
print(books[middle_index - 1:middle_index + 2])

print(f"The last three items in the list are:")
print(books[-3:])  # Using negative indexing to get the last three items
# Output:
# The first three items in the list are:
# ['The Great Gatsby', 'To Kill a Mockingbird', '1984']
# Three items from the middle of the list are:
# ['To Kill a Mockingbird', '1984', 'Pride and Prejudice']
# The last three items in the list are:
# ['1984', 'Pride and Prejudice', 'The Catcher in the Rye']
