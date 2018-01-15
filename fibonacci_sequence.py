def fibonacci():
	number = int(input("Enter a number: "))
	sequence = [0,1]
	a = 0
	b = 1
	while b < number:
		c = b+a
		sequence.append(c)
		a = b
		b = c
		
	print (sequence)
fibonacci()
		
		
