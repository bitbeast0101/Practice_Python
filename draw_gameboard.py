def board():
	rows = int(input("enter number of rows :"))
	columns = int(input("enter number of columns:"))
	i = 0
	box = rows
	if rows == columns:	
		while i < rows:
			print((" " + "-"*3)*rows)
			
			print(("|"+" "*3)*rows+"|")
			
			
			i += 1
		print((" " + "-"*3)*rows)	
	else:
		print("not symmetrical")
board()
				
