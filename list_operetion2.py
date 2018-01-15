def common_list():
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	a1 = []
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	b1 = []
	com = []
	for element in a:
		if element not in a1:
			a1.append(element)
	print(a1)
	for element2 in b:
		if element2 not in b1:
			b1.append(element2)
	print(b1)
	for element in a1:
		if element in b1:
			com.append(element)
	print("Elements common in list",com)
common_list()
