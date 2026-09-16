"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a "while True" loop to remain awake.
[ ] 3. Main menu uses match-case logic for selections.
[ ] 4. Inputs are validated (e.g., .isdigit()) to prevent crashes (include try except)
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

try:
    # >greater <less
    # variables
    choice = 1
    balance = 1000
    withdraw = 0
    deposit = 0

    while choice > 0 and choice < 4:
        print(f"1. View balance")  # menu will constantly display after asking a choice
        print(f"2. Withdraw")
        print(f"3. Deposit")
        print(f"4. Exit")
        print("")
        choice = int(input("Please enter the number of you selection: "))

        match choice:
            case 1:
                print(f"Your balance is ${balance:.2f} ")
                print("")
            case 2:
                withdraw = input(
                    "Please enter the amount you would like to withdraw: "
                )  # Setting it up so .isdigit() works

                while (
                    not withdraw.isdigit()
                ):  # repeats question/statement until valid input
                    print("that was not a valid number \n")
                    withdraw = input(
                        "Please enter the amount you would like to withdraw: "
                    )

                withdraw = float(withdraw)  # Turns the withdraw into a num

                if withdraw > balance:  # still needed
                    print("You do not have the sufficient balance to withdraw this.")
                    print("")
                else:
                    balance = balance - withdraw
                    print(f"you withdrew ${withdraw:.2f}")
                    print(f"Your new balance is {balance:.2f}")
                    print("")
            case 3:
                deposit = int(input("How much would you like to deposit: "))
                if deposit < 0:
                    print("Sorry, this is an invalid amount to deposit \n")
                else:
                    balance = balance + deposit
                    print(f"You have deposited ${deposit:.2f}")
                    print(f"Your new balance is ${balance:.2f}\n ")
            case 4:
                print("")
                print("Good Bye!")


except ValueError:
    print("Please enter a number")
except Exception as e:  # captures unknown errors
    print(e)
