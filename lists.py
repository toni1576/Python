# Lists, arrays, vectors, tuples

# Python - lists are mutable, tuples are immutable
# other languages have arrays and vectors

# create list

dwarves = ["Doc", "Grumpy", "Happy", "Sleepy", "Bashful", "Sneezy", "Dopey"]  # 0-6

# for dwarf in dwarves:  # prints them individual
#     print(dwarf)


# college_classes = [
#     "intro to psychology",
#     "Calculus I",
#     "World History",
#     "General History",
#     "English Composition",
#     "Microeconomics",
#     "intro to programming",
#     "Spanish II",
#     "Organic Chem",
#     "Stats"
# ]


# for item in college_classes:
#     print(item)

# #removes matching values
# try:
#     college_classes.remove("Calculus I")
#     for item in college_classes:
#         print(item)
# except ValueError:
#     print("Sorry this is not in my list")

# print(len(college_classes))


# # if "Sleepy" in dwarves:
# #     print("Yes, Sleepy is a dwarf")

# vertically_challenged = dwarves
# #vertically_challenged = dwarves [:]
# for person in vertically_challenged:
#     print(person)


# vertically_challenged.append("Snarky")

# for dwarf in dwarves:
#     print(dwarf)

v_c = dwarves[:]

# v_c.append("Sarcastic")

# for dwarf in v_c:
#     print(dwarf)

v_c.sort()

for dwarf in v_c:
    print(dwarf)
