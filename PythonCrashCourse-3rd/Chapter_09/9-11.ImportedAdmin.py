"""
9-11. Imported Admin:
Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module.
Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
"""

from modules.PrivilegesModule import User, Admin, Privileges

hadi = Admin('Abdullah', 'Hadi', 'hadi7452', 'admin')
hadi.describe_user()

hadi.privileges.privileges = ['can add post', 'can delete post', 'can ban user', 'can moderate comments', 'can invite users']
hadi.privileges.show_privileges()