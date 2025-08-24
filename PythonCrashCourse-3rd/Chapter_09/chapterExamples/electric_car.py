# Inheritance
# The __init__() Method for a Child Class

class Car:
    def __init__(self, make, model, year):
        self.tank_size = None
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        self.tank_size = 10
        print(f"The car has {self.tank_size} tank size.")


class Battery:
    # A simple attempt to model a battery for an electric car

    def __init__(self, battery_size=40):
        # Initialize the battery's attributes.
        self.battery_size = battery_size

    def describe_battery(self):
        # Print a statement describing the battery size.
        print(f"This car has a {self.battery_size}-kwh battery size.")

    def get_range(self):
        # Print a statement about the range this battery provides.
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge")
# Creating a child Class
class ElectricCar(Car):
    # Represents aspects of a car, specific to electric vehicles.

    def __init__(self, make, model, year):
        # Initialize attributes of the parent class.
        super().__init__(make, model, year)
        self.battery = Battery()

    #     # Initialize attributes specific to an electric car.
    #     self.battery_size= 40
    #
    # def describe_battery(self):
    #     print(f"This car has {self.battery_size}-kWh battery.")

    # Overriding Methods from the Parent Class
    def fill_gas_tank(self):
        print(f"This Electric Car doesn't have a gas tank")

my_leaf = ElectricCar("Nissan", "Leaf", 2024)
print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()
# my_leaf.fill_gas_tank()

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()