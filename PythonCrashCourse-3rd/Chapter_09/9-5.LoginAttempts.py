"""
9-5. Login Attempts:
Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162).
Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0.
"""

class User:

    def __init__(self, first_name, last_name, user_id, user_type):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.user_type = user_type

        # Creating Loging Attempts
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nPrinting User Summary:")
        print(f"\t- Full Name: {self.first_name} {self.last_name}")
        print(f"\t- User ID: {self.user_id}")
        print(f"\t- User Type: {self.user_type}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}, You are {self.user_type} user!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Creating instance of User Class
user = User('Abdullah', 'Hadi', 'hadi17', 'student')

# Calling increment login attempts several times
user.increment_login_attempts()
print(f"Login Attempts made: {user.login_attempts}")

user.increment_login_attempts()
print(f"Login Attempts made: {user.login_attempts}")

user.increment_login_attempts()
print(f"Login Attempts made: {user.login_attempts}")

user.increment_login_attempts()
print(f"Login Attempts made: {user.login_attempts}")

# Resetting Loging Attempts
user.reset_login_attempts()
print(f"Login Attempts reset to : {user.login_attempts}")

# Increment login attempts again
user.increment_login_attempts()
print(f"Login Attempts made: {user.login_attempts}")