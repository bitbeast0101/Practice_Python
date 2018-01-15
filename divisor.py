def divisor():
	num = int(input("enter a number: "))
	i = 1
	while i <= int(num/2):
		if num % i == 0 :
			print(i)
			
		i += 1
divisor()
