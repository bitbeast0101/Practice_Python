def palindrome():
	string = input("Enter the string: ")
	string = string.lower()
	print(string)
	rev_string = "".join(reversed(string))
	print(rev_string)
	if string == rev_string:
		print("Its a palindrome")
	else:
		print("Not a palindrome")
palindrome()
