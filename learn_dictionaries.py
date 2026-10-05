#Dictionaries
#you are allowed to use AI to fill dictionaries with data, add a comment to say you did
#Dictionaries use curly braces {}

import random

# Created with AI assistance.
french_numbers = {
    1: "un",
    2: "deux",
    3: "trois",
    4: "quatre",
    5: "cinq",
    6: "six",
    7: "sept",
    8: "huit",
    9: "neuf",
    10: "dix",
}

quiz = list(french_numbers.items())
random.shuffle(quiz)

# #looks in keys the number on the side of the dictionary --------------------
# if 6 in french_numbers:
#     print("Found!")

# else:
#     print("Not found!")

# #I give it a key (the number on the side of the dictionary), gives the corresponding value ---------------------
# print(french_numbers[3])

# #creates or update, if it exists we replace it ----------------------------
# french_numbers[11] = "onze"

# #Delete an item ------------------
#french_numbers.pop(0)

# #error - key error ------------------
# try:
#     print(french_numbers[14])
# except KeyError:
#     print("This is not in our dictionary")

# #better ------------
# answer = french_numbers.get[12]
# print(answer)

#quiz
correct = 0
incorrect = 0
for key, value in quiz:
    answer = int(input(f"Please enter the numeric value for {value}: "))
    if answer == key:
        print("correct")
        correct +=1
    else:
        print("incorrect")
        incorrect += 1

score = correct/10
print(f"Score: {score:.1f}")
