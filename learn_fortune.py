
# Advance strings, import statements, random

import random


fortunes = [
    "You will ace your next exam. Your pencil already believes in you.",
    "Your group project will have one useful group member. It might be you.",
    "A professor will say, 'This won't be on the test,' and mean it.",
    "Your next all-nighter will be interrupted by a very responsible nap.",
    "You will find a quiet study spot, right after everyone else does.",
    "A forgotten assignment will reveal itself five minutes before the deadline.",
    "Your coffee will be strong, your Wi-Fi stronger, and your essay submitted.",
    "You will raise your hand with confidence—and ask the exact right question.",
    "Your laundry will achieve sentience before you run out of clean socks.",
    "The dining hall will serve your favorite meal on the day you brought lunch.",
    "You will remember your password just after resetting it.",
    "Your alarm won't go off. Fortunately, your roommate's will—and so will they.",
    "A textbook will cost less than your monthly snack budget. Probably.",
    "You will open one tab to study and somehow discover 37 tabs later.",
    "Your future is bright, though your laptop battery is at 3 percent.",
    "You will make it to class early, only to discover class was canceled yesterday.",
    "The vending machine will accept your dollar and offer valuable life lessons.",
    "You will conquer finals week, one questionable snack at a time.",
    "Your notes will be beautifully organized. Finding them is a separate challenge.",
    "You will graduate with honors—or at least with all your chargers.",
]

# selected = random.randint(0, 24)
# print(fortunes[selected])
#---------------------------------------

topic = input("Please enter a single word that you want to use to look for fortunes. ").lower().strip()

printed = False

for item in fortunes:
    item = item.lower()
    if topic in item:
        printed = True
        print(item)
        break

if printed == False:
    selected = random.randint(0, 19)
    print(fortunes[selected])