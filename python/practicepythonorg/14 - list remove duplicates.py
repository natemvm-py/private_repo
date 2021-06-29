#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

#Extras:
#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function

ages = [12, 12, 15, 15, 21, 47, 47, 47]	
removed_duplicates_list = []

print('Unsorted List:', ages)

#Function that removes duplicates using the 'set()' function.
def removeDuplicates_set(list):
	removed_duplicates = set() #Creating a variable with the set data type.
	for i in list: #For each value in given list.
		removed_duplicates.add(i) #Add to the variable 'removed_duplicates'. Sets in their own nature will not allow duplicates so it will automatically remove duplicates for you.
	return removed_duplicates #Returns the set to the function.


#Extra, function with a loop that creates another list, NOT a set.
def removeDuplicates_list(list):
	for i in list: #For each value in given list.
		if i not in removed_duplicates_list: #and if said value does not already exist in the new list.
			removed_duplicates_list.append(i) #Append said value to the new list.
	return removed_duplicates_list #Returning the list to the function.
	
print('Sorted with set():', removeDuplicates_set(ages))

print('Sorted with lists:', removeDuplicates_list(ages))
