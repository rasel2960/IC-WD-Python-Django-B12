"""
9-12. Multiple Modules:
Store the User class in one module, and store the Privileges and Admin classes in a separate module.
In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
"""

from modules.AdminPrivilegesClass import Admin, Privileges

ayesha = Admin('Rufaydah', 'Ayesha', 'ayesha23', 'admin')
ayesha.describe_user()

ayesha.privileges.privileges = ['can add post', 'can delete post', 'can ban user', 'can moderate comments', 'can invite users']
ayesha.privileges.show_privileges()