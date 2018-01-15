def even_or_odd():
	number = int(input("Enter number: "))
	if number % 2 == 0:
		print("even number")
		if number % 4 == 0:
			print("Also divisible by 4")
	else:
		print("odd number")
even_or_odd()
	
