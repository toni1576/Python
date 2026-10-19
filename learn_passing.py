#Passing values with functions

#GLOBALS



SCOPE_DEMO = "Visible!"

def passed (variable):
    #Notice the name does not matter
    print(variable)

def not_passed():
    #print(local)
    #print(variable)
    print(SCOPE_DEMO)

def count(one, two, three = 3):
    print(one)
    print(two)
    print(three)

def control(one, two, three):
    print("\n\ncontrol")
    print(one)
    print(two)
    print(three)


def main():
    print(SCOPE_DEMO)
    local = "Can you see me?"
    print(local)
    passed(local)
    not_passed()
    count(4, 32,)
    control(three = 3, two = 2, one = 1)

main()