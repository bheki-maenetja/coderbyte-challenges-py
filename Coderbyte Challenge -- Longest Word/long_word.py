def LongestWord(sen): 
	#Removes any non-alphabetic characters.
    word_list = []
    for word in sen.split():
    	if word.isalpha():
    		word_list.append(word)
    	else:
    		new_string = ""
    		for i in word:
    			if i.isalpha():
    				new_string += i
    		word_list.append(new_string.strip())
    #Finds longest word
    sen = ""
    for word in word_list:
    	if len(word) > len(sen):
    		sen = word 
    print(sen)
      
LongestWord(input("Enter anything: "))

# <-- Updated Version -->

def LongestWord(sen):
    for i in sen:
        sen = sen.replace(i, "") if not i.isalpha() and i != " " else sen
    sen = sen.split()
    print(f"The longest word in this sentence is:\n {max(sen, key=len)}")

LongestWord(input("Enter anthing: "))

















  