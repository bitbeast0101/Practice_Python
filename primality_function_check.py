def divisor(num):
	
	i = 2
	factors = []
	while i <= int(num/2):
		if num % i == 0 :
			factors.append(i)		
		i += 1
	print("Divisors are: ",factors)
	if factors == []:
		print("prime number")
	else:
		print("not prime number")

def primality_check():
	num = int(input("Enter a number: ")
divisor()
primality_check()
	
	


	
