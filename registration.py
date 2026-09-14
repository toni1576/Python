"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# >greater <less

fn_ln = ""
while not fn_ln:
    fn_ln = input("Please enter your first and last name: ")

age = -1
while age < 0:
    age = int(input("Please enter your age: "))


phone_num = 0
while phone_num > 9:
    phone_num = int(input("Please enter your phone number: "))
