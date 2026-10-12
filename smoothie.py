"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

# TODO: Define get_price(size)
def get_price(size):
    match size.lower():
        case "small":
            return 3.0
        case "medium":
            return 4.0
        case "large":
            return 5.0
        case _:
            print("Invalid entry")
            return 0.0

# TODO: Define blend(size, base, fruit, scoops)
def blend(size, base, fruit, scoops):

    price = get_price(size)
    total_price = price + (scoops * 0.5)
    print(f"Your smoothie: {size} with {base} and {fruit}, {scoops} scoops")
    print(f"Total price: ${total_price:.2f}")


# TODO: Define main() to collect input and call your logic
def main():
    size = input("What size smoothie do you want (Small, Medium, Large): ")
    base = input("What base do you want? (Water, Apple Juice, Orange Juice, Milk):  ")
    fruit = input("What fruit do you want? (Strawberry, Banana, Mango, Blueberry):  ")

    try:
        scoops = int(input("How many scoops? "))
    except ValueError:
        print("Scoops must be a whole number.")
        return

    if get_price(size) == 0.0: # Check if the size is invalid
        return

    blend(size, base, fruit, scoops) # Call the blend function with the collected inputs



main()