"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
"""
#task 1 tuning guitar
instrument = "Acoustic Guitar"
print(len(instrument))
print(instrument[0] + instrument[14])
lowest = min(instrument)
highest = max(instrument)
print(lowest)
print(highest) #consider done for now

print("/\n")

#task 2 cleanup crew
messy_input = "   vOLUME_knob_11   "
print(messy_input.strip().replace("_", " ").title())

print("/\n")

#task 3 the validator
serial_number = "90210"
if serial_number.isdigit():
	print("Valid serial")
else:
	print("Invalid serial")

print("/\n")

# task 4 the duck bridge 
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0
print("\n--- Singing the Duck Song ---")
for character in duck_letters:
	current_name = " ".join(duck_letters)
	print("There was a teacher who had a duck and Ducky was his Name-o")
	print(f"({current_name}) \n" *3)
	print("and Ducky was his Name-o! \n")
	duck_letters[count] = " 🦆"
	count += 1
#final
final_name = " ".join(duck_letters)
print(f"{final_name}")
