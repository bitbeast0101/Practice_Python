def listop():
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = []
	index = 0
	for element in a:
		if a[index] < 5:
			print(a[index])
			b.append(a[index])	
		index += 1
	print(b)
	number = int(input("enter a number: "))
	index = 0
	for element in a:
		if a[index] < number:
			print(a[index])
			b.append(a[index])	
		index += 1
	print(b)
listop()
