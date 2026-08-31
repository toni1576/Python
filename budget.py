"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

# Variables
gross_income = ""
groceries = ""
electric_bill = ""
pets = ""
water_bill = ""
gas = ""

print("")
# Input of expenses
gross_income = float(input("What is your gross Monthly Income? "))
groceries = float(input("How much do you spend monthly on groceries? "))
electric_bill = float(input("How much do you spend monthly on your electric bill? "))
pets = float(input("How much do you spend monthly on your pets? "))
water_bill = float(input("How much do you spend monthly on your water bill? "))
gas = float(input("How much do you spend monthly on gas? "))

print("")
# Net Income |Total Expenses | Remaining Balance
net_income = gross_income * 0.8
total_expense = groceries + electric_bill + pets + water_bill + gas
remaining_balance = net_income - total_expense

# Percent of income spent
income_spent = net_income % total_expense

# Output formatted decimal places
print(f"Gross income = {gross_income: ,.2f}")
print(f"Total expenses = {total_expense: ,.2f}")
print(f"Remaining balance = {remaining_balance: ,.2f}")
print(f"Percent of Income spent = {income_spent: ,.2f}")
print("")
