names = "Tony"

new_name = "Tom"

names =  names + new_name # replaces content of names

print(names)

print("*" * 50)

print(len(names)) #print the length of the string

print(names[3]) #print the character at index 3
print(f"\n\n - 2 blank lines \n \t tabs")

my_name = "   mark     karma       "
print(my_name.strip().title()) # Strip removes white space, title() capitalizes the first letter of each word

greeting = "Hello, World!"
words = greeting.split(" ") # Split the greeting into a list of words
print(words) # Print the list of words

for word in words: #print each word of the list separately
    print(word)


print("Is Alpha")
print("Python".isalpha())
print("Python!".isalpha()) # Check if the string contains only alphabetic characters

name_string = "BINGO"
dog_letters = list(name_string) # Convert the name string into a list of characters
count = 0
for char in name_string:
    current_name = " ".join(dog_letters)
    print("There was  a farmer who had a dog and Bingo was his Name-o")
    print(f"({current_name}) \n" *3)
    print("and Bingo was his Name-o \n")
    dog_letters[count] = "👏"
    count += 1    
#final
final_name = " ".join(dog_letters)
print(f"({final_name})")

