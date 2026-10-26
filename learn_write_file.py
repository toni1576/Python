#Writing to files

#timestamp
import time


#create and write to a file

def write_header():
    # file =  open("menu.txt", "w")
    # file.write("------------Coffee menu------------")
    # file.close | Old way

    #New way
    with open("menu.txt", "w") as f:
        f.write(f"{right_now}")
        f.write("-------- Specials --------\n")


def append_lines():
    with open("menu.txt", "a") as f:
        f.write()


def main():
    write_header()

main()