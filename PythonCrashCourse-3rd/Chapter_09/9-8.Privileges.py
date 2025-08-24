"""
9-8. Privileges:
Write a separate Privileges class.
The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class.
Make a Privileges instance as an attribute in the Admin class.
Create a new instance of Admin and use your method to show its privileges.
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
        self.privileges = Privileges()


class Privileges:

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            print(f"Admin user enjoys the following privileges: ")
            for privilege in self.privileges:
                print(f"\t- {privilege.title()}")
            else:
                print("\t- The user has no privileges")

ayesha = Admin('Rufayadah', 'ayesha', 'ayesha23', 'admin')
ayesha.describe_user()

ayesha.privileges.show_privileges()

print(f"Adding privileges....")
ayesha.privileges.privileges = ['can add post', 'can delete post', 'can ban user', 'can moderate comments', 'can invite users']
ayesha.privileges.show_privileges()