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


# class Admin(User):
#     def __init__(self, first_name, last_name, user_id, user_type):
#         super().__init__(first_name, last_name, user_id, user_type)
#         self.privileges = Privileges()
#
#
# class Privileges:
#
#     def __init__(self, privileges=[]):
#         self.privileges = privileges
#
#     def show_privileges(self):
#         if self.privileges:
#             print(f"Admin user enjoys the following privileges: ")
#             for privilege in self.privileges:
#                 print(f"\t- {privilege.title()}")
#         else:
#             print("\t- The user has no privileges")
