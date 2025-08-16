# 8-5. Cities:
# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as Reykjavik is in Iceland.
# Give the parameter for the country a default value.
# Call your function for three different cities,
# at least one of which is not in the default country.

def describe_city(city, country='Bangladesh'):
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('dhaka')
describe_city(city="Rangpur")
describe_city(city='Khulna', country='Bangladesh')
describe_city(country='england', city='london')



