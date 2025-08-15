# 7-10. Dream Vacation:
# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.

dream_vacation = {}
poll_active = True

while poll_active:
    name = input('What is your name? ')
    location = input("If you could visit one place in the world, where would you go? ")
    dream_vacation[name] = location

    # Keep asking for yes/no until valid
    while True:
        repeat = input("Would you like to poll for another person? (yes/no) ")
        if repeat.lower() == 'no':
            poll_active = False
            break
        elif repeat.lower() == 'yes':
            break
        else:
            print(f"Please enter either 'yes' or 'no'")

print("\n---- Results ----")
for name, location in dream_vacation.items():
    print(f"{name.title()} would like to visit {location.title()} someday")

