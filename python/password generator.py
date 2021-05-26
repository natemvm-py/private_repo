import random

def spec_randGen():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p = "".join(random.sample(s,passLength))
    print(p)
    
def randGen():
    m = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = "".join(random.sample(m,passLength))
    print(n)


def main():    
    specialAllow = input("Include Special Characters? (e.g. !@#$), Y/N: ")
    if (specialAllow == "Y" or specialAllow == "y"):
        spec_randGen()
    elif(specialAllow == "N" or specialAllow == "n"):
        randGen()
    else:
            print("Incorrect Input!")
            main()


while(True):
    try:
        passLength = int(input("Enter desired length of password: "))
    except ValueError or SyntaxError or NameError or TypeError:
        print("Please only enter an integer value. (e.g. 1234)")
        continue
    else:
        main()


