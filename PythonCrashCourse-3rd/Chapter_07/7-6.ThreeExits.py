# 7-6. Three Exits:
# Write different versions of either Exercise 7-4 or 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

prompt = "\nWelcome to the movie theater!"
prompt += "\nPlease enter your age to find out the cost of your movie ticket. "
prompt += "\n(Enter 'quit' to exit.) "

active = True
while active:
    age = input(prompt)

    if age.lower() == 'quit':
        break

    # check if input is an integer (including negative numbers)
    if not age.lstrip('-').isdigit():
        print("You must enter a valid age or 'quit' to exit.")
        continue
    age = int(age)

    if age < 0:
        print("\nAge cannot be negative. Exiting the program.")
        active = False

    elif 0 < age < 3:
        print("\nYour movie ticket is free!")
    elif 3 <= age < 12:
        print(f"\nYour movie ticket is $10.")
    elif age >= 12:
        print(f"\nYour movie ticket is $15.")
    else:
        print("\nInvalid age entered. Please try again.")
