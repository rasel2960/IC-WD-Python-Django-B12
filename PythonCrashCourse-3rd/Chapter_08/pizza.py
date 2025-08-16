# This is a module created for example codes of Chapter 08 (Functions)

def make_pizza(size, *toppings):
    # Summarize the pizza we are about to make.
    if not toppings:
        print(f"\nMaking a {size}-inch pizza without toppings.")
    else:
        print(f"\nMaking a {size}-inch pizza with the following toppings:")
        for topping in toppings:
            print(f"\t- {topping.title()}")


