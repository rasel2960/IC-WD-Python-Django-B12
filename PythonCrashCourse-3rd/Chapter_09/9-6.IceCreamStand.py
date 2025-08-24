"""
9-6. Ice Cream Stand:
An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166).
Either version of the class will work; just pick the one you like better.
Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.
"""

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name.title()}' has a cuisine of '{self.cuisine_type.title()}'")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print(f"My favorite ice-cream flavors are: ")
        for flavor in self.flavors:
            print(f"\t- {flavor}")

icecreamFlavors = IceCreamStand('Thie Big One', 'Ice Cream')
icecreamFlavors.describe_restaurant()

icecreamFlavors.flavors = ['almond joy', 'bacon', 'birthday cake', 'apple pie', 'bavarian cream']
icecreamFlavors.display_flavors()