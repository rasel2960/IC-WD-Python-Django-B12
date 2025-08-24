"""
9-7. Admin:
An administrator is a special kind of user.
Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167).
Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of privileges.
Create an instance of Admin, and call your method.
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
        print(f"\nUser Summary:")
        user_summary = {'Full Name' : self.first_name + ' ' + self.last_name, 'User ID' : self.user_id, 'User Type' : self.user_type}
        print(f"\t- {user_summary}")
        # print(f"\t- Full Name: {self.first_name} {self.last_name}")
        # print(f"\t- User ID: {self.user_id}")
        # print(f"\t- User Type: {self.user_type}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}, You are {self.user_type} user!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, user_id, user_type):
        super().__init__(first_name, last_name, user_id, user_type)
        self.privileges = []

    def show_privileges(self):
        print(f"Admin user enjoys the following privileges: ")
        for privilege in self.privileges:
            print(f"\t- {privilege.title()}")

# Creating instance of User Class
hadi = Admin('Abdullah', 'Hadi', 'hadi17', 'admin')
hadi.describe_user()

hadi.privileges = ['can add post', 'can delete post', 'can ban user', 'can moderate comments', 'can invite users']
hadi.show_privileges()
# # Calling increment login attempts several times
# user.increment_login_attempts()
# print(f"Login Attempts made: {user.login_attempts}")
#
# user.increment_login_attempts()
# print(f"Login Attempts made: {user.login_attempts}")
#
# user.increment_login_attempts()
# print(f"Login Attempts made: {user.login_attempts}")
#
# user.increment_login_attempts()
# print(f"Login Attempts made: {user.login_attempts}")
#
# # Resetting Loging Attempts
# user.reset_login_attempts()
# print(f"Login Attempts reset to : {user.login_attempts}")
#
# # Increment login attempts again
# user.increment_login_attempts()
# print(f"Login Attempts made: {user.login_attempts}")