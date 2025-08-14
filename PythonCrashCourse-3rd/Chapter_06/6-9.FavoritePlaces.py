# Make a dictionary called favorite_places.
# Think of three names to use as keys in the dictionary, and
# store one to three favorite places for each person.
# To make this exercise a bit more interesting,
# ask some friends to name a few of their favorite places.
# Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    'rasel': ['Dhaka', 'Tangail', 'Chittagong'],
    'hadi': ['Tangail', 'Sylhet', 'Rajshahi'],
    'shishir': ['Dhaka', 'Chittagong', 'Khulna'],
}

# ask some friends to name a few of their favorite places with input
for name in favorite_places.keys():
    places = input(f"Hello, {name.title()}, Write your favorite places (separated by commas): \n\t> ")
    new_places = [place.strip() for place in places.split(',') if places.strip()]

    favorite_places[name].extend(new_places)

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t- {place.title()}")

