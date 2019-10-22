def MyReverse(word):
	return_string = ""
	word_list = word.split()
	for word in word_list:
		word = word.strip()
		newWord = ""
		for i in range(len(word) - 1, -1, -1):
			newWord += word[i]
		word_list[word_list.index(word)] = newWord 
	for i in range(len(word_list) - 1, -1, -1):
		return_string += word_list[i] + " "
	print(return_string)

#MyReverse(input("Enter a string: "))

# <-- Updated Version -->

def MyReverse(word):
	return_string = ""
	word_list = [i for i in word]
	word_list.reverse()
	for i in word_list:
		return_string += i
	print(return_string)

MyReverse(input("Enter a string: "))