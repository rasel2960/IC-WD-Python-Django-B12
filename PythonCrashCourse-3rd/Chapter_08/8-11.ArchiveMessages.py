# 8-11. Archived Messages:
# Start with your work from Exercise 8-10.
# Call the function send_messages() with a copy of the list of messages.
# After calling the function, print both of your lists to show that the original list has retained its messages.

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    print(f"\nSending all Messages...")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ["I'm learning Python.", 'Learning Python is awesome.', 'My ultimate goal is to be a Python Data Scientist.']
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal Message List:")
print(messages)
print(sent_messages)