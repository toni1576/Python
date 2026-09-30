"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""
import random

# Create a tuple of possible Magic 8 Ball responses.
RESPONSES = (
	"Yes",
	"No",
	"Maybe",
	"Ask again later",
	"Definitely",
	"It is unlikely",
	"Without a doubt",
	"Possibly",
)

print("")
print("Welcome to the Digital Oracle!")
ask = True

while ask:
    question = input("Please ask a yes or no question, type 'quit' to end: ")
    if "quit" in question.lower():
        ask = False
    else:
        print(random.choice(RESPONSES))
        print("")

# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop
