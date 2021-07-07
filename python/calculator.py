input1 = 0
input2 = 0
operator = ""
result = 0

print("Welcome to calculator")

while(True):
    input1 = int(input("Enter first number: "))

    operator = input("Enter desired operator (+,-,*, or /): ")

    input2 = int(input("Enter second number: "))

    if operator == "+" or operator == "plus":
        result = input1 + input2
        print(input1, " + ", input2, " = ", result)
    elif operator == "-" or operator == "minus":
        result = input1 - input2
        print(input1, " - ", input2, " = ", result)
    elif operator == "*" or operator == "times":
        result = input1 * input2
        print(input1, " x ", input2, " = ", result)
    elif operator == "/" or operator == "divide" or operator == "÷" or operator == "":
        result = input1 / input2
        print(input1, " ÷ ", input2, " = ", result)
    else:
        print("Unexpected error, please tell Nate")
