while(True):
    year = int(2024)
    name = str(input("name:"))
    age = int(input('age:'))

    if(age > 99):
        print('no siree')
    else:
        age = int(age)

        foundYear = year + (100 - age)
        foundYear = str(foundYear)

        count = int(input('count:'))
    
        newString = str('ur name is ' + name + ' and you will turn 100 in the year ' + foundYear + "\n")
    
        print(count * newString)