"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""
TOPPINGS = ("pepperoni", "mushrooms", "onions", "sausage", "bacon")

#line 17-20, in main() print out the info user inputted in a summary format.
def make_pizza(toppings, customer, size, is_delivery=False):
    print("Welcome to the Resilient Pizza Engine!")
    print(f"{customer} ordered a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

    #check if is_delivery true or false and print the 2 different prints.
    if is_delivery:
        print("This pizza will be delivered.")
    else:
        print("This pizza will be picked up.")


def main():
    print("")
    print("Welcome to the Resilient Pizza!")
    customer = input("What is your name? ")
    size = input("What size pizza would you like? (Small, Medium, Large): ")

    print(f"Available toppings: {TOPPINGS}")
    requested_toppings = input(
        "Which toppings would you like? Separate multiple toppings with commas: "
    )
    toppings = tuple(
        topping.strip().lower()
        for topping in requested_toppings.split(",") 
    )#.split(",") makes it so that each chosen topping can be created as a separate item in the tuple and print them.

    delivery_answer = input("Should the pizza be delivered? (yes/no): ")
    is_delivery = delivery_answer.strip().lower() in ("yes", "y")
    #line 44 checks if the user input is a yes with .strip and .lower to account for case sensitivity allowing no errors. "yes" and "y" take into account shortened responses.

    print("")
    print("---------Order Summary---------")
    make_pizza(
        toppings=toppings,
        customer=customer,
        size=size,
        is_delivery=is_delivery,
    )
    print("---------End of Order Summary---------")
    print("")



main()