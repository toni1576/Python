# answer = int(input("Enter a number between 1 and 100: "))
# # == compares the answer to if statement
# if answer == 42:
#     print("You found the answer to life, the universe and everything")
# else:
#     print("Sorry talk to the white mice.")


# int turns string into a Whole number while float accepts decimals
print("Score must be numeric: 90, 90.5")
score = float(input("Please enter your test score: "))

if score > 90.0:
    print("A")
elif score > 80.0:
    print("B")
elif score > 70.0:
    print("C")
elif score > 60.0:
    print("D")
else:
    print("F")


# Stings are case sensitive
# .lower() will take Wednesday and wednesday the lower case option
current_month = input("What Month is it? (Month name): ")

match current_month.lower():
    case "september":
        print("labor Day")
