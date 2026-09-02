"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [09/02/26]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask the user for their age (convert to int) and the day of the week (convert to string).
2. if day is tuesday child prices are .5 per year of age otherwise it is 1 - match******
Calculate the base price using if/elif/else:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. ask user age*****
Use a match/case statement to handle special daily rules based on the day entered:
   - Tuesday: Children through age 12 are half price!
   - Sunday: Drinks are free!
   - Other days: Standard buffet pricing in effect.
4. if elsif to determine price****
Print the final price formatted as currency and display any applicable daily special notices.
-----------------------------------------------------------------------
"""

# variables

user_age = int(input("What is your age? (As a number): "))
week_day = input("What day of the week is it?: ")

# day idk
match week_day.lower():
    case "tuesday":
        child_price_per_year = 0.5

    case "sunday":
        print(f"Drinks are free")
    # used for anything/other input
    case _:
        child_price_per_year = 1

# Statements >greater <less
if user_age < 1:
    print("FREE")
elif user_age <= 12:
    print(f"{child_price_per_year * user_age}")
elif user_age <= 64:
    print("$16.95")
else:
    print("$12.95")
