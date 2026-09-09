"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

# >Greater <less
if num1 & num2 > 0:
    print("Both are greater than zero!")
else:
    print("Both are less than zero!")

print()  # 1/6

if num1 & num2 > 100:
    print("both are greater than 100")
else:
    print("both are less than 100")

print()  # 2/6

if num1 % 2 == 0:  # check for num1 1/3
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")

print()  # 3/6

if num2 % 2 == 0:
    print(f"{num2} is even")
else:
    print(f"{num2} is odd")

print()  # 4/6

if num1 < 100:  # check for num1 2/3
    print(f"{num1} is less than 100")
else:
    print(f"{num1} is greater than 100 ")

print()

if num1 != num2:
    print("The numbers are not equal")
else:
    print("The numbers are equal")

print()  # 5/6

if num1 != 0:  # check for num1 3/3
    print(f"{num1} is not 0")
else:
    print(f"{num1} is 0")

if num2 != 0:
    print(f"{num2} is not 0")
else:
    print(f"{num2} is 0")
# 6/6
