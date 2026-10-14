"""
Final project - step 1
Copy as a new step with new comment each week
This week: Define constants, create stubs, create menu

"""

# Globals - variables declared outside of all of the functions are global
# Constants (still globals)  - don't change while project is running
SIZES = ("Small", "Medium", "Large", "X-Large")
MILKS = ("Oat", "Soy", "Coconut", "Whole", "2%", "Skim")
PRICES = {"Small": 3.50, "Medium": 5.00, "Large": 7.00, "Extra Large": 9.00}
MENU = "menu.txt"


# Program Functions

def login():
    # Gets login info
    # returns employee ID
    print("Please login")
    id = int(input("Please enter your employee ID: "))
    #have employee text with ID and names check if on it. If on it display name, office, extension otherwise get them. 
    
    pass

def past_orders(employee):
    # check for and display most recent 5 orders if there are any, ask if they want to reorder, give them menu
    # return number of past order or 6 if they want to create a new order
    pass

def new_order(employee):
    # display choices, collect information, save and pass back a LIST named order
    pass

def verify(order):
    # verify order by displaying on screen and asking confirm, correct, cancel
    pass

def save_order(order):
    # save to txt file
    pass

def change_order(order):
    #Display numbered parts of order allow them to change
    pass

def display_order(order):
    #in real world would create label
    pass


# Main traditionally is coded at the end of the page so the other functions are loaded first
def main():
    # main organizes all of the functions 
    id = login()
    saved = past_orders(id)
    # if saved order chosen  skip new order
    order = new_order(id)
    approved = verify(order)
    #if approved save - otherwise change
    save_order(order)
    change_order(order)
    display_order(order)


main()    