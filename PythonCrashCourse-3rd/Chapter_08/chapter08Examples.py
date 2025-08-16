""" Defining a Function """
def greet_user():
    # Display a simple greeting
    print("Hello!")
greet_user()

""" Passing Information to a Function """
def greet_user(username):
    # Display a simple greeting.
    print(f"Hello, {username.title()}!")
greet_user('rasel')
greet_user('hadi')

""" Passing Positional Arguments """
def describe_pet(animal_type, pet_name):
    # Display information about a pet
    print(f"\nI have a {animal_type}.")
    print(f"\tMy {animal_type}'s name is {pet_name.title()}.")

# Multiple Function Calls
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Order Matters in Positional Arguments
describe_pet('harry', 'hamster')

# KeyWord Arguments
describe_pet(animal_type='dog', pet_name='willie')
describe_pet(pet_name = 'harry', animal_type = 'hamster')

""" Default values in Parameters """
def describe_pet(pet_name, animal_type='dog'):
    # Display information about a pet
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

""" Equivalent Function Calls """
# Because Positional Arguments, Keyword Arguments and Default Values can all be used together
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('Willie')
describe_pet(pet_name='Willie')


""" Return Values """
# Returning a Simple Value
def get_formatted_name(first_name, last_name):
    # Return a full name, neatly formatted.
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('andrew', 'kishore')
writer = get_formatted_name(last_name='Matthes', first_name='Eric')
print(musician)
print(writer)
print(musician, "-", writer)

# Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=''):
    # Return a full name, neatly formatted.
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('andrew', 'kishore')
writer = get_formatted_name(last_name='Matthes', first_name='Eric')
student = get_formatted_name('abdullah', 'hadi', 'al')
player = get_formatted_name(middle_name='lee', last_name='hooker', first_name='James')
print(musician)
print(writer)
print(player)
print(student)

""" Returning a Dictionary """
def build_person(first_name, last_name):
    # Return a dictionary of information about a person.
    person = {'first_name': first_name, 'last_name' : last_name}
    return person
musician = build_person('Abdullah', 'Hadi')
teacher = build_person('Nadia', 'Ayesha')
print([musician, teacher])

# Extend previous function to accept optional values like middle name or age
def build_person(first_name, last_name, middle_name ='', age=None,):
    # Return a dictionary of information about a person
    person = {'first_name': first_name, 'middle_name' : middle_name, 'last_name' : last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('Abdullah', 'Hadi', middle_name='Al', )
teacher = build_person('Nadia', 'Ayesha', age= 35)
print([musician, teacher])

""" Using a Function with a while Loop """
def get_formatted_name(first_name, last_name):
    # Return a full name, neatly formatted
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# while loop to greet people using their first and last names
while True:
    print(f"\nPlease tell me your name: ")
    print(f"Enter 'q' at any time to quit")

    f_name= input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name.title()}")

""" Passing a List """


def greet_users(names):
    # A simple function that greets each person in the list individually
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'hadi', 'margot']
greet_users(usernames)

""" Modifying a List in a Function """
def print_models(unprinted_designs, completed_models):
    # Simulate printing each design, until none are left
    # Move each design to completed_models after printing.

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing {current_design.title()}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    # Show all the models that were printed
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model.title())

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

""" Preventing a Function from Modifying a List """
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f"- {completed_model}")

unprinted_designs = ['phone case', 'robot pendant', 'key ring']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

""" Passing an Arbitrary Number of Arguments """
def make_pizza(*toppings):
    # print the list of toppings that have been requested
    print(f"\nMaking a Pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


""" Mixing Positional and Arbitrary Arguments """
def make_pizza(size, *toppings):
    # summarize the pizza we are about to make

    if not toppings:
        print(f'\nMaking a {size}-inch pizza without any toppings:')

    else:
        print(f'\nMaking a {size}-inch pizza with the following toppings.')
        for topping in toppings:
            print(f'\t- {topping.title()}')
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cesse')
make_pizza(20)

""" Using Arbitrary Keyword Arguments """
def build_profile(first, last, **user_info):
    # Build a dictionary containing everything we know about a user.
    user_profile = {
        'first_name' : first.title(),
        'last_name' : last.title(),
    }
    user_info.update(user_profile)
    return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'pyhsics')
print(user_profile)


""" Storing Your Functions in Modules """
''' Importing an Entire Module '''
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
pizza.make_pizza(14)

"""Importing Specific Functions """
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(14)

""" Using 'as' to Give a Function an 'Alias' """
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
mp(14)

""" Using as to Give a Module an Alias """
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12)
p.make_pizza(13, 'green chesse', 'banh hee')

""" Importing All Functions in a Module """
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12)
make_pizza(13, 'green chesse', 'banh hee')
