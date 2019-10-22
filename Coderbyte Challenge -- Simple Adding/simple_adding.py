def SimpleAdding(num):
	return_num = 0
	for i in range(1, num + 1):
		return_num += i
	print(return_num)

SimpleAdding(int(input("Enter any number: ")))