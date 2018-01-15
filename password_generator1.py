def password_generator1():
	psswd = ""
	count = 0
	for i in range(65,90):
		count += 1
		psswd = psswd + (chr(i))
		if count > 4:		
			break
		
	for i in range(97,122):
		count += 1
		psswd = psswd + (chr(i))
		if count > 7:		
			break
		
	for i in range(48,57): 
		count += 1
		psswd = psswd + (chr(i))
		if count > 12:		
			break
		psswd.join(chr(i))
	for i in range(33,126):
		count += 1
		psswd = psswd + (chr(i))
		if count > 14:		
			break
		psswd = psswd + (chr(i))
	print(psswd)
password_generator1()
