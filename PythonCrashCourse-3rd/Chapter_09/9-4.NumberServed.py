"""
9-4. Number Served:
Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class.
Print the number of customers the restaurant has served,
and then change this value and print it again.

    Add a method called set_number_served() that lets you set the number of customers
that have been served. Call this method with a new number and print the value again.

    Add a method called increment_number_served() that lets you increment the number
of customers who’ve been served. Call this method with any number you like that
"""

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

        # Adding an attribute that counts the number served
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The '{self.restaurant_name.title()}' serves wonderful '{self.cuisine_type.title()}'.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open.")

    def set_number_served(self, number_served):
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print("You can't roll back from previously served customer.")

    def increment_number_served(self, inc_number_served):
        self.number_served += inc_number_served

# Making an instance of Restaurant Class
restaurant = Restaurant("Korai Gosto", "Kacchi")
restaurant.describe_restaurant()

# Printing the number of customers the restaurant has served
print(f"Number of Customer's Served: {restaurant.number_served}")

# Changing Customer Served Value
restaurant.number_served = 15
print(f"Number of Customer's Served: {restaurant.number_served}")


# Calling set_number_served() to show how many customers received service from the Restaurant

restaurant.set_number_served(24)
print(f"Number of Customer's Served: {restaurant.number_served}")

# Updating Customer Number Served by incrementing to previously served number
restaurant.increment_number_served(15)
print(f"Number of Customer's Served: {restaurant.number_served}")

# Testing if it rolls back from previously served customer
restaurant.set_number_served(24)
print(f"Number of Customer's Served: {restaurant.number_served}")

# Updating Customer Number Served by incrementing to previously served number
restaurant.increment_number_served(11)
print(f"Number of Customer's Served: {restaurant.number_served}")