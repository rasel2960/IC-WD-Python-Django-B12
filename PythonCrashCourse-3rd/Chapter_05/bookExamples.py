# Checking That a List Is Not Empty

requested_toppings = ['peperoni']

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print(f"\nFinished making your pizza")
else:
    print(f"Are you sure you want a plain pizza?")

print("\n\n")
# Using Multiple Lists
availabe_toppings = ['mushrooms', 'olive','green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in availabe_toppings:
        print(f"Adding {requested_topping.title()}")
    else:
        print(f"Sorry, we don't have {requested_topping.title()}")
print("\nFinished making your pizza!")
 