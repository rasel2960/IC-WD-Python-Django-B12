# 8-9. Messages:
# Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints each text message.

def show_messages(msg):
    for message in messages:
        print(message)

messages = ["I'm learning Python.", 'Learning Python is awesome.', 'My ultimate goal is to be a Python Data Scientist.']
show_messages(messages)