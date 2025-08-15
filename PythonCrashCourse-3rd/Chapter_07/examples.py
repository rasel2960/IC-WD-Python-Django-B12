# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
#
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")
#
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}")
#
# prompt = "If you tell us who you are, we can personalize the messages you see.\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}")
#
#
""" Using int() to Accept Numerical Input """
# age = input("How old are you? ")
# age = int(age)
# print(age)
# print(age >= 18)
#
""" A simple program that determines whether people are tall enough to ride a roller coaster. """
# height = input("How tall are you, in inches? ")
# height = int(height)
#
# if height >= 48:
#     print(f"\nYou're tall enough to ride!")
# else:
#     height_short = 48 - height
#     print(f"\nYou're {height_short} inches short from the required height of 48 inches to ride.")


""" simple program to determine if a number is even or odd """
# number = input("Enter a number and I'll tell you if it's even or odd: ")
# number = int(number)
#
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")
#

""" The wile loop in Action """
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
""" Letting the User Choose When to Quit """
# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)
#
""" updated version of the immediate program """
# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
#
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

""" Using a Flag """
# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#
#     if message.lower() == 'quit':
#         active = False
#     else:
#         print(message)

""" Using break to Exit a Loop """
#
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
#
# while True:
#     city = input(prompt)
#     if city.lower() == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

""" Using continue in a Loop """
# # for example: consider a loop that counts from 1 to 10 but prints only the odd numbers:
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

""" Moving Items from One List to Another """
#
# # Start with users that need to be verified,
# # and an empty list to hold confirmed users.
#
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
#
# # Verify each user until there are more unconfirmed users.
# # Move each verified user into the list of confirmed users.
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
#
# # Display all confirmed users:
# print(f"\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(f"\t- {confirmed_user.title()}")

""" Removing All Instances fo Specific Values from a List """
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

""" Filling a Dictionary with User Input """
responses = {}

# Set a flat to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to clib someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")