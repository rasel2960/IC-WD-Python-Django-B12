# Working with Classes and Instances

# The Car Class
class Car:
    # A simple attempt to represent a car

    def __init__(self, make, model, year):
        # Initialize attributes to describe a car.
        self.make = make
        self.model = model
        self.year = year

        # Setting a Default Value for an Attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        # Print a statement showing the car's mileage
        print(f"This car has {self.odometer_reading} miles on it.")

    # Modifying an Attribute's Value Through a Method
    def update_odometer(self, mileage):
        # Set the odometer reading to the given value.
        # Set additional logic to make sure no one tries to roll back the odometer reading
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back an odometer!")

    # Incrementing an Attributes Value Through a Method
    def increment_odometer(self, miles):
        # Add the given amount to the odometer reading
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an Attribute's Value Directly
my_new_car.odometer_reading = 30
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an Attribute's Value Through a Method
my_new_car.update_odometer(25)
my_new_car.read_odometer()

# Incrementing an Attributes Value Through a Method
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
