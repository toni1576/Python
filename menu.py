print(f"1. Create new contact")
print(f"2. Search contact")
print(f"3. Update contact")
print(f"4. Delete contact")
print(f"5. Quit")

choice = 1

choice = int(input("Please enter the number of your selection:  "))

while choice > 0 and choice < 4:
    match choice:
        case 1:
            print("Create")
        case 2:
            print("Search")
        case 3:
            print("Update")
        case 4:
            print("Delete")
        case 5:
            print("Good bye!")
# IT keeps repeating an option
