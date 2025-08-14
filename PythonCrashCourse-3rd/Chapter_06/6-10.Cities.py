# Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and
#  - include the country that the city is in,
#  - its approximate population, and
#  - one fact about that city.
#  The keys for each city’s dictionary should be something like country, population, and fact.
#  Print the name of each city and all the information you have stored about it.

cities = {
    'tangail': {
        'country': 'bangladesh',
        'population': 500000,
        'fact': 'Tangail is famous for its handloom products.',
    },
    'london': {
        'country': 'united kingdom',
        'population': 8908081,
        'fact': 'London is known for its iconic landmarks like the Big Ben and the Tower of London.',
    },
    'new york': {
        'country': 'united states',
        'population': 8419600,
        'fact': 'New York City is often referred to as "The Big Apple"',
    },
}

for city, info in cities.items():
    country = info['country'].title()
    population = info['population']
    fact = info['fact'].capitalize()

    print(f"\n{city.title()} is in {country}.")
    print(f"\tIt has a population of approximately {population:,} people.")
    print(f"\tImportant fact : {fact}")
