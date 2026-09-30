# while loop
# calculating average test score
entering = True  # flag
total = 0
count = 0

while entering:
    print("Enter the test score, enter -1 when done")
    score = float(input("Enter the test score: "))
    if score > 0:
        total += score  # short cut total = total plus score
        count += 1
    else:
        entering = False

average = total / count

print(f"The average test score was: {average:,.if}")

# print all numbers leading to the last number but wont count up to the last
for x in range(1, 10):
    print(x)

for y in range(10, 0, -1):
    print(y)

# # Will print out all text in the string list unlike in numbers
for day in "Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday":
    print(day)

eat = False

while not eat:
    feed = input("can we eat now?   (yes/no)   ").lower
    if feed == "yes":
        eat = True
