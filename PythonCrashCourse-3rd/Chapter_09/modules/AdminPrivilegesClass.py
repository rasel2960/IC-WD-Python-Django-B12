from .UserClass import User

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
