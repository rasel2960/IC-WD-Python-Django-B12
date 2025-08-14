# 6-1. Person:
# Use a dictionary to store information about a  person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.
person = {
    'first_name': 'Abdullah',
    'last_name': 'Hadi',
    'age': 8,
    'city': 'Tangail',
}
print(f"First Name: {person['first_name'].title()}")
print(f"Last Name: {person['last_name'].title()}")
print(f"Full Name: {person['first_name'].title()} {person['last_name'].title()}")
print(f"Age: {person['age']}")
print(f"City: {person['city'].title()}")

