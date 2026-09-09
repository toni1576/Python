"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

nagging = False

while not nagging:
    stop = input("Are we there yet? (yes/no) ").lower()
    if stop == "yes":
        nagging = True

print()

# >Greater <less
for beer in range(99, 1, -1):
    print(f"{beer} bottles of beer on the wall!")
    if beer < 3:
        print("1 bottle of beer on the wall!")
