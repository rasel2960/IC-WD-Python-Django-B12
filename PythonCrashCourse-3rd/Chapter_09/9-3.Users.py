"""
9-3. Users:
Make a class called User.
Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
"""

class User:

    def __init__(self, first_name, last_name, user_id, user_type):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.user_type = user_type

    def describe_user(self):
        print(f"\nPrinting User Summary:")
        print(f"\t- Full Name: {self.first_name} {self.last_name}")
        print(f"\t- User ID: {self.user_id}")
        print(f"\t- User Type: {self.user_type}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}, You are {self.user_type} user!")

user1 = User("Rasel", "Ahmed", "symoon", "admin")
user1.describe_user()
user1.greet_user()

user2 = User("Rufaydah", "Ayesha", "baitullah10", "kidz")
user2.describe_user()
user2.greet_user()

user3 = User('Abdullah', 'Hadi', 'hadi19', 'student')
user3.describe_user()
user3.greet_user()

