import random
def check_game():
	first_row = []
	second_row = []
	third_row = []	
	matrix = [first_row,second_row,third_row]
	i,j = 0,0
	while i <= 2:
		first_row.append(random.randint(1,2))
		second_row.append(random.randint(1,2))
		third_row.append(random.randint(1,2))
		i += 1
	print(matrix)
	
	flag = 0
	i,j = 0,0
	
	while i < 3:
		if matrix[i][0] == matrix [i][1] and matrix[i][1] == matrix[i][2]:
			
			if matrix[i][0] == 1:
				print("Player 1 wins")
			elif matrix[i][0] == 2:
				print("Player 2 wins")
			quit()
		
		i += 1
		
	i = 0
	while j <= 2:
		if matrix[i][j] == matrix[i+1][j] and matrix[i+1][j] == matrix[i+2][j]:
			
			if matrix[i][j] == 1:
				print("Player 1 wins")
			elif matrix[i][j] == 2:
				print("Player 2 wins")
			quit()
		j += 1

	i,j = 0,0

	if matrix[i][j] == matrix[i+1][j+1] and matrix[i+1][j+1] == matrix[i+2][j+2]:
		
		if matrix[i][j] == 1:
			print("Player 1 wins")
		elif matrix[i][j] == 2:
			print("Player 2 wins")
		
	else:
		print("No winner")
				
	
		
		
check_game()	
		 

