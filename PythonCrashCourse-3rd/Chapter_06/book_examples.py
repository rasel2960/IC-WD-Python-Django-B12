# Programs used as examples in the book

alien_0 = {'color': 'green', 'points': 5}

print(alien_0["color"].title())
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {alien_0['points']} points!")
print(alien_0)
alien_0['x_position'] = 0
alien_0["y_position"] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

print("\n")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

print("\n")
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3


print(f"Original position: {alien_0['x_position']}")
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# delete multiple keys from a dictionary while storing them in a separate dictionary at the same time.

# A dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sahrah' favorite language is {language}.")
print()

# Using get() to access values in a dictionary
alien = {'color': 'green', 'points': 5, 'speed': 'medium'}
print(alien.get('color', 'No color provided.').title())
print(alien.get('name', 'No name provided.').title())

print()

# A list of Dictionaries
alien0 = {'color': 'green', 'points': 5, 'speed': 'medium'}
alien1 = {'color': 'yellow', 'points': 10, 'speed': 'fast'}
alien2 = {'color': 'red', 'points': 15, 'speed': 'slow'}

aliens = [alien0, alien1, alien2]

for alien in aliens:
    print(alien)

# A list in a dictionary
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# A dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username.title()}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    loaction = user_info['location'].title()
    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {loaction}")
