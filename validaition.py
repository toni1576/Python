# Error checking data entry with while statements

# name Check
# Rules - Can't be empty, less than 30 characters, first letter should capitalize (we can do that for them)
try:
    fname = ""
    while not fname:
        fname = input("Please enter your first name:  ")
    fname = fname.strip()

    age = -1
    while age < 0:
        age = int(input("Please enter your child's age (whole years, round down):  "))

except ValueError:
    print("I'm sorry, that is not a valid value")
except Exception as e:
    print(f"Error: {e}")
