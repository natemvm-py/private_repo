#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
#The passwords should be random, generating a new password every time the user asks for a new password. 
#Include your run-time code in a main method.

#Extra:
#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

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
