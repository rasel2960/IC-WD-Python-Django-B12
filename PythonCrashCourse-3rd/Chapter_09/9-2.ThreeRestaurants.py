"""
9-1. Restaurant:
Make a class called Restaurant.
The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods.
"""

"""
9-2. Three Restaurants:
Start with your class from Exercise 9-1.
Create three different instances from the class, and call describe_restaurant() for each instance.
"""
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name.title()}' has a cuisine of '{self.cuisine_type.title()}'")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open.")

# Making an instance of Restaurant Class
restaurant1 = Restaurant("Korai Gosto", "Kacchi")
restaurant2 = Restaurant("Xinxian", "Thai Soup")
restaurant3 = Restaurant("KFC", "Fried chicken")

# Calling describe_restaurant() method
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


