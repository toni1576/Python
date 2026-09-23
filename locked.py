"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

try:
    DEP_ELECTRONICS = "Electronics Department"
    USER_NAMES = ("John", "Tess", "May", "Tom", "Terry")
    passwords = ["12345", "12345", "12345", "12345", "12345"]
    choice = 1

    while choice > 0 and choice < 4:
        print("1. Update Passwords")
        print("2. Test Security")
        print("3. Look up Employee")
        print("4. Quit \n")
        choice = int(input("Please enter the number of your selection: "))
        print("")

        match choice:
            case 1:
                name = input(
                    "Please enter the user name of who's password your changing: "
                )
                if name in USER_NAMES:
                    location = USER_NAMES.index(name)
                    password = input("Enter a new password: ")
                    passwords[location] = password
                    print("Password has been changed \n")
                else:
                    print("Sorry This user doesn't exist \n")
            case 2:
                user = input("What would you like to change your user name to? ")
                USER_NAMES[0] = user

            case 3:
                look = input(
                    "Please enter the name of the employee you want to look for: "
                )

            case 4:
                print("Goodbye!")

except ValueError:
    print("Please enter a number")
except TypeError:
    print("User names cannot be changed. Please email the help desk.")
except Exception as e:
    print(e)
