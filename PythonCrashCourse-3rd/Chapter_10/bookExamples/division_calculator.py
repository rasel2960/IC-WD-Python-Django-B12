# # Using try-except to handle division by zero
# try:
#     print(5/0)  # ZeroDivisionError: division by zero
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# Using Exception to Prevent Crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    # The else Block
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("Please enter valid numbers.")
    else:
        print("Answer is:", answer)

