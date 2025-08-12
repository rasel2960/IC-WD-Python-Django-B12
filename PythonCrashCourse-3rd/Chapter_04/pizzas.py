# Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
pizzas = ['pepperoni', 'mushroom', 'sausage']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print(f"\nI really love pizza!")

print("\n")
# 4-11. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# - Add a new pizza to the original list.
# - Add a different pizza to the list friend_pizzas.
# - Prove that you have two separate lists. Print the message 'My favorite pizzas are:'
#   Then use a for loop to print the first list. Print the message 'My friend's favorite pizzas are:'
#   Then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

friend_pizzas = pizzas[:]
pizzas.append('new Pizza')
friend_pizzas.append('different Pizza')
print(pizzas)
print(friend_pizzas)

print("\n")
print(f"My favorite pizzas are:")
print(pizzas)

print(f"\nMy friend's favorite pizzas are:")
print(friend_pizzas)

print(f"\nMy favorite pizzas are:")
for pizza in pizzas:
    print("\t",pizza)
print(f"\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("\t",pizza)
