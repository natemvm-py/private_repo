#Write a program (using functions!) that asks the user for a long string containing multiple words. 
#Print back to the user the same string, except with the words in backwards order.

#Function that reverses the sentence.
def reverseSentence(sentence):
	split = sentence.split() #Splits all words at every whitespace and assigns it to the list variable: 'split'.
	split.reverse() #Reverses the list.
	reversedSentence = ' '.join(split) #Joins each item in the list with a space and assignts it to the variable: 'reversedSentence'.
	return reversedSentence #Returns the reversedSentence variable to the function.
	
print(reverseSentence(input('Enter a sentence: ')))