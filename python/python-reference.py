#Variables - Essentially a box to store information inside of. We then name that box and can call that name at any time in order to use the information stored inside that variable.
print('---VARIABLES---')
char_name = 'Nate' #String value - Always inside of single or double quotes. Python only sees this. E.g. If you had '10' (Pay attention to the quotes surrounding the 10) stored inside a variable, python wont see this as an integer/number but instead a string/word.
char_age = 20 #Integer value - a number value that does not consist of a decimal point.
char_weight = 61.2 #Float value - a number value that includes a decimal point.
char_alive = True #Boolean value - either True or False

#Variables names are case sensitive, keep that in mind.
print('---VARIABLES & CASE SENSITIVITY---')
a = 1 #a will not override A
A = 2 #A will not override a
print('VARIABLE: \'a\' = ' + str(a))
print('VARIABLE: \'A\' = ' + str(A))

#Data types - Python doesnt view the same characters as the same 'object'.
print('---DATA TYPES---')
b = 10 #Python sees this as a number that can be used in addition, subtraction, etc etc.
B = '10' #Python will only see this as a string. You cannot use this variable to add numbers up because python doesn't view this as an integer value. Python see's this as a STRING. A.K.A a word not a number.
print(type(b))
print(type(B))
#To provide an example to aboves comment, Unhash this line of code and you will always get an error from a python interpreter. This is because python cannot add a number and a word together, that just simply doesn't make any sense.
#sum = b + B

#Using Variables inside of Strings - Including other data types, e.g. int, bool, float.
print('---USING VARIABLES INSIDE OF STRINGS - INCLUDING OTHER DATA TYPES---')
print('My name is: ' + char_name + '. I am: ' + str(char_age) + ' Years Old.') #str(char_age) = Python cannot concatenate an integer value to a string, therefore it needs to be converted to a string in order to work.
print('Nate is: ' + str(char_weight) + ' Kilograms') #str(char_weight) = Python cannot concatenate a float value to a string, there it needs to be converted to a string in order to work.
print('Is ' + char_name + ' currently Alive?: ' + str(char_alive)) #str(char_alive) = Python cannot concatenate a boolean value to a string, therefore it needs to be converted in order to work.

#In order to use other data types within strings without having to convert them, use ',' instead of '+'.
print('---USING OTHER DATA TYPES WITHIN STRINGS W/OUT CONVERSION---')
print('An example:', char_age)

#Getting the Variables Type
print('---GETTING THE VARIABLE TYPE---')
print(type(char_name))
print(type(char_age))
print(type(char_weight))
print(type(char_alive))

#Converting Variables Type
print('---CONVERTING VARIABLES TYPE---')
exampleVariable = 10
print(type(exampleVariable))
exampleVariable = str(exampleVariable) #Converts into a String data type.
print(type(exampleVariable))
exampleVariable = int(exampleVariable) #Converts into an Integer data type.
print(type(exampleVariable))
exampleVariable = float(exampleVariable) #Converts into a Float data type.
print(type(exampleVariable))
exampleVariable = bool(exampleVariable) #Converts into a Boolean data type.
print(type(exampleVariable))

#Operators - Used to perform operations on variables and values.

#Arithmetic Operators
print('---ARITHMETIC OPERATORS---')
a = 3 #Example Variable
b = 2 #Example Variable
c = 0 #Example Variable
c = a + b #Addition
print('a + b =', c)
c = a - b #Subtraction
print('a - b =', c)
c = a * b #Multiplication
print(a * b)
c = a / b #Division
print(a / b)
c = a % b #Modulus - Gives remainder of two numbers.
print(a % b)
c = a ** b #Exponentiation - To the power of.
print(a ** b)
c = a // b #Floor Division - Essentially cuts off the decimal.
print(a // b)

#Assignment Operators
a = 3 #Assigns a value to a variable.
a += 1 #Plus Equals 1 = Adds 1 to the already existing value of that variable instead of just reassigning the variable.
a -= 1 #Minus Equals 1 = Subtracts 1 from the already existing value of that variable.
a *= 1 #Mulitply Equals 1 = Multiplies 1 by the already existing value of that variable.
a /= 1 #Divide Equals 1 = Divides 1 by the already existing value of that variable.
a %= 1 #Modulus Equals 1 = Gives the remainder of 1 comapared to the already existing value of that variable.
