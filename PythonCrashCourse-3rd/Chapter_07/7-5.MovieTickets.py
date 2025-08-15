# 7-5. Movie Tickets:
# A movie theater charges different ticket prices depending on a person’s age.
# If a person is under the age of 3, the ticket is free;
# if they are between 3 and 12, the ticket is $10; and
# if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, and
# then tell them the cost of their movie ticket.

prompt = "\nWelcome to the movie theater!"
prompt += "\nPlease enter your age to find out the cost of your movie ticket. "
prompt += "\n(Enter 'quit' to exit.) "

while True:
    age = input(prompt)

    if age.lower() == 'quit':
        break

    age = int(age)
    if 0 < age < 3:
        print("\nYour movie ticket is free!")
    elif 3 <= age < 12:
        print(f"\nYour movie ticket is $10.")
    elif age >= 12:
        print(f"\nYour movie ticket is $15.")
    else:
        print("\nInvalid age entered. Please try again.")
