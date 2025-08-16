# 8-13. User Profile:
# Start with a copy of user_profile.py from page 148.
# Build a profile of yourself by calling build_profile(),
# using your first and last names and three other key-value pairs that describe you.

def user_profile(first_name, last_name, **kwargs):
    # Build a dictionary of a user profile
    user_info = {
        'first_name' : first_name.title(),
        'last_name' : last_name.title(),
    }
    kwargs.update(user_info)
    return kwargs

user_profile = user_profile('rasel', 'ahmed', sex = 'male', age = 37, profession = 'banker')
print(user_profile)