"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

# >greater <less
seats = list(range(1, 21))

while seats:
	print("Available seats:", seats)
	choice = int(input("Choose a seat number (0 to quit): "))

	if choice == 0:
		print("Goodbye!")
		break # exit the loop
	elif choice in seats:
		seats.remove(choice) #removes the seat chosen 
		print(f"Seat {choice} reserved.")
	elif 1 <= choice <= 20:
		print(f"Seat {choice} is already taken.")
	else:
		print(f"Seat {choice} does not exist.")

if not seats: # not makes the condition true when seats are all taken
	print("All seats are reserved.")