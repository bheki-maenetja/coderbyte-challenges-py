def FirstFactorial(num):
	org = 1
	for i in range(1, num+1):
		org *= i
	num = org
	return num
     
#print(FirstFactorial(raw_input()))
for i in range(1, 101):
	print(f"{i}'s factorial is {FirstFactorial(i)}")
