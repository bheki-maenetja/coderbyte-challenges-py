def LetterChanges(word):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	letterList = []
	for i in word:
		letterList.append(i)
	for i in range(0, len(letterList)):
		if letterList[i].isalpha():
			letterList[i] = alphabet[alphabet.index(letterList[i]) + 1] if letterList[i] != "z" else "a"
	word = ""
	for i in letterList:
		word += i
	vowelList = "aeiou"
	for i in word:
		word = word.replace(i, i.upper()) if i in vowelList else word
	print(word)
	


LetterChanges("abcdefghijklmnopqrstuvwxyz")