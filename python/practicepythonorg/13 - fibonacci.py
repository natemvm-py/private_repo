#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
#Take this opportunity to think about how you can use functions. 
#Make sure to ask the user to enter the number of numbers in the sequence to generate.
#(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

#Function to generate fibonaacci numbers.
def gen_fib():
	count = int(input('Enter count: '))
	
	i = 1 #Used to count
	
	if count == 0:
		fib = []
	elif count == 1:
		fib = [1]
	elif count == 2:
		fib = [1, 1]
	elif count > 2:
		fib = [1, 1]
		while i < (count -1):
			fib.append(fib[i] + fib[i-1]) #Adds together the i'th index number + the last number in the list and appends it to a list.
			i += 1 #We add 1 so that the while loop works correctly and also so that we keep moving along the index of the list.
			
	return fib #Returns the list.
	
print(gen_fib()) #We print the function so it prints the fib list.