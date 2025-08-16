# 8-4. Large Shirts:
# Modify the make_shirt() function so that shirts are large by default with a message
# that reads I love Python.
# Make a large shirt and a medium shirt with the default message,
# and a shirt of any size with a different message.

def make_shirt(size='large', message='I love Python'):
    print(f"\nI'm going to make a '{size}' size T-Shirt")
    print(f"and It'll have the message: '{message.upper()}' on it")


make_shirt()
make_shirt('small')
make_shirt('medium', 'Something Good is going to happen')
make_shirt(size='large')

