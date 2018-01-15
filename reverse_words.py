def reverse_words() :
	
	string = input("Enter a sentence to be reversed: ")
	string_list = string.split() 								#splitting on all white spaces
	reverse_string = ""
	for token in string_list:
		reverse_string = token +" "+ reverse_string
	print (reverse_string)

reverse_words()
