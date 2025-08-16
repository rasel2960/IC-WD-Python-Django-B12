# 8-12. Sandwiches:
# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function call provides,
# and it should print a summary of the sandwich that’s being ordered.
# Call the function three times, using a different number of arguments each time.

def ordered_sandwich(*items):
    print(f"\nThe following sandwiches have been ordered:")
    for item in items:
        print(f"\t- {item.title()}")
    print(f"Your ordered sandwich(es): {items} are ready.")

ordered_sandwich('barros luco', 'bauru')
ordered_sandwich('beef on week', 'baros jarpa', 'bagel toast', 'banh mi')
ordered_sandwich('barbecue')
