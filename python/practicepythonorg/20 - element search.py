import random

list = []

for i in range(10):
    list.append(random.randint(1,99))

list.sort()
print(list)

def find_element(userGuess):
    if userGuess in list:
        return True
    else:
        return False

while(True):
    print(find_element(int(input('Enter Guess: '))))
