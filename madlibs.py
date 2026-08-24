"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Copy and paste THIS comment from)
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# 1. variables (5)
name = ""
animal = ""
color = ""
food = ""
season = ""
animal_name = ""

# User Input and assign to variables
print("")
name = input("Please enter a person's name: ")
animal = input("Please enter a type of animal: ")
animal_name = input("Please enter a name for your animal: ")
color = input("Please enter a color: ")
food = input("Please enter your favorite food: ")
season = input("Please enter your favorite season: ")

# Output
print("")
print(f"Would you like to introduce yourself {name}?\n\n")
print(f"Hi, my name is {name} and my favorite color is {color},")
print(f"A favorite food of mine is {food} and my favorite season is {season}")
print(f"and I have an {animal} and their name is {animal_name}!")
print("")
