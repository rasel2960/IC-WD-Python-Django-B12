# 7-4. Pizza Toppings:
# Write a loop that prompts the user to enter a series of pizza toppings
# until they enter a 'quit' value.
# As they enter each topping, print a message
# saying you’ll add that topping to their pizza.

prompt = "Which toppings would you like to add in your pizza? "
prompt += "\n(Enter 'quit' when you are finished adding toppings.) "
toppings_list = []
while True:
    pizza_toppings = input(prompt)
    if pizza_toppings.lower() == 'quit':
        break
    else:
        toppings_list.append(pizza_toppings)
        print(f"\nI'm adding {pizza_toppings.title()} to your pizza!\n")
print(f"\nYou have added {toppings_list} toppings in your pizza")
print("and your pizza is ready!")
