import random
sorted_arr = []
count = 0
while count <= 10:
	num = random.randint(1,10)
	sorted_arr.append(num)
	count += 1
sorted_arr = sorted(sorted_arr)
duplicate = sorted_arr
print(sorted_arr)


def linear_search():
	element = int(input("enter element to be searched:"))
	
	if element in sorted_arr:
		print (True)
	else:
		print (False)	
#linear_search()

def binary_search():
	element = int(input("enter element to be searched:"))
	arr_size = len(sorted_arr)
	print(arr_size)
	flag = 0
	while flag == 0:
		if element > sorted_arr(arr_size/2):
			duplicate = duplicate[(arr_size/2):]
		else:
			duplicate = duplicate[:(arr_size/2)]
		if duplicate == [element]:
			flag = 1
			print(duplicate)	

binary_search()





