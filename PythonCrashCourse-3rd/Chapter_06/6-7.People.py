"""
6-7. People:
Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all
three dictionaries in a list called people. Loop through your list
of people. As you loop through the list, print everything you know
about each person.
"""

people = []
person1 = {
    'first_name': 'Abdullah',
    'last_name': 'Hadi',
    'age': 8,
    'city': 'Tangail',
}
people.append(person1)

person2 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',
}

people.append(person2)
person3 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles',
}

people.append(person3)

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    print(f"{full_name} is {person['age']} years old and live in {person['city'].title()}.")

