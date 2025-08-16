# 8-14. Cars:
# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs,
# such as a color or an optional feature.
# Your function should work for a call like this one:
#       car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary

def make_car(manufacturer, model_name, **key_features):
    car_info = {
        'manufacturer' : manufacturer.title(),
        'model_name' : model_name.title(),
    }
    key_features.update(car_info)
    print(f"\nCar Information:")
    return key_features

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = make_car('honda', 'accord', production_year=1991, color='white', headlights='popup')
print(car)
