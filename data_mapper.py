"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[ ] 3. Program takes a word and uppercases it.
[ ] 4. Program loops through letters and prints NATO words.
[ ] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""
try:
    #Created with AI assistance.
    NATO_ALPHABET = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-ray",
        "Y": "Yankee",
        "Z": "Zulu",
    }
    NATO_TO_LETTER = {code.upper(): letter for letter, code in NATO_ALPHABET.items()}
    choice = 1
    print("")

    while choice > 0 and choice < 3:
        print(f"1. Enter English")
        print(f"2. Enter coded word")
        print(f"3. Exit")
        print("")
        choice = int(input("Enter your choice: "))
        print("")
        # word = input("Enter word to spell: ").upper()

        match choice:
            case 1: #user input get turned into the nato code and print it out
                word = input("Enter word to spell: ").upper() 
                for letter in word:
                    try:
                        print(NATO_ALPHABET[letter])
                        print("")
                    except KeyError:
                        print(f"Unknown letter: {letter}")
                        print("")

            case 2: #user input NATO code is converted back to English and printed out
                coded_word = input(
                    "Enter NATO words separated by spaces: "
                ).upper().split() # 
                english_word = ""
                for code in coded_word:
                    try:
                        english_word += NATO_TO_LETTER[code]
                    except KeyError:
                        print(f"\nUnknown NATO word: {code}")
                print(english_word)
                print("")

            case 3: #leaves the program
                print("Goodbye!")
                break

    # TODO: Loop through each character
    # TODO: try to print the NATO code, except if character is missing
except ValueError:
    print("Please enter a number")
except Exception as e:
    print(f"An error occurred: {e}")