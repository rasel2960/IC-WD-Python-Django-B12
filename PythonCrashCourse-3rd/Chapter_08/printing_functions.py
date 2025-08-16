""" Preventing a Function from Modifying a List """
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f"- {completed_model.title()}")

unprinted_designs = ['phone case', 'robot pendant', 'key ring']
completed_models = []