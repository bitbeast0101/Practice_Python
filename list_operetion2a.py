import random
def common_list():
	a = []
	for element in range(10):	
		a.append(random.randint(1,100))
	print (a)
	a1 = []
	b = []
	for element2 in range(12):
		b.append(random.randint(1,100))
	print (b)
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
	com = [element for element in a1 if element in b1]
	print(com)
common_list()
