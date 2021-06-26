#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

str = input('Word: ')

rvsStr = str[::-1]

print(rvsStr)

if rvsStr == str:
    print('Is Palindrome')
else:
    print('Is Not Palindrome')
    