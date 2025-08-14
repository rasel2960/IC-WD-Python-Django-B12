# Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as you do,
# print everything you know about each pet.
pets = []
pet = {
    'animal_type': 'mammals',
    'owner': 'Abdullah Hadi',
    'pet_name': 'Tommy',
    'age': 2,
    'city': 'Tangail',
}
pets.append(pet)

pet = {
    'animal_type': 'bird',
    'owner': 'John Doe',
    'pet_name': 'Tweety',
    'age': 1,
    'city': 'New York',
}
pets.append(pet)
pet = {
    'animal_type': 'fish',
    'owner': 'Jane Smith',
    'pet_name': 'Goldie',
    'age': 1,
    'city': 'Los Angeles',
}
pets.append(pet)

# Display information about each pet in text format
for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['animal_type']} named {pet['pet_name'].title()}.")
    print(f"{pet['pet_name'].title()} is {pet['age']} years old and lives in {pet['city'].title()}.")
    print()

# Display information about each pet in dictionary format
for pet in pets:
    print(f"\nInformation about {pet['pet_name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key.title()} : {value.title() if isinstance(value, str) else value}")
