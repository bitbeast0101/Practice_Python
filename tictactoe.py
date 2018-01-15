import random
def tictactoe_game():
	game = [['0','0','0'],
		['0','0','0'],
		['0','0','0']]
	
	draw_tictactoe(game)
	check_game(game)

def board(game):
	rows = 3
	columns = 3
	i = 0
	j = 0
	
	
		
	while i < rows:
		print((" " + "-"*3)*rows)
	
		print(("|"+" "+game[i][j]+" ")+("|"+" "+game[i][j+1]+" ")+("|"+" "+game[i][j+2]+" ")+"|")
		i += 1
	
	print((" " + "-"*3)*rows)	
	
def draw_tictactoe(game):
	
	count = 0
	while count <= 8:
		if count % 2 == 0:
			print("PLayer 1 plays")
		else:
			print("player 2 plays")
		user_input = input("enter row and coloumn:")
		user_input = user_input.split(",")
		row,col = int(user_input[0]),int(user_input[1])
		
		if game[row][col] == 'x' or game[row][col] == 'o':
			
			print("Occupied")
			print(count)
			continue
		else:
			if count % 2 == 0:
				game[row][col] = 'x'
			else:	
				game[row][col] = 'o'
		print(count)
		count += 1
		board(game)


def check_game(game):
	first_row = game[0]
	second_row = game[1]
	third_row = game[2]	
	matrix = [first_row,second_row,third_row]
	print(matrix)
	i,j = 0,0
	
	while i < 3:
		if matrix[i][0] == matrix [i][1] and matrix[i][1] == matrix[i][2]:
			
			if matrix[i][0] == 'x':
				print("Player 1 wins")
			elif matrix[i][0] == 'o':
				print("Player 2 wins")
			quit()
		
		i += 1
		
	i = 0
	while j <= 2:
		if matrix[i][j] == matrix[i+1][j] and matrix[i+1][j] == matrix[i+2][j]:
			
			if matrix[i][j] == 'x':
				print("Player 1 wins")
			elif matrix[i][j] == 'o':
				print("Player 2 wins")
			quit()
		j += 1

	i,j = 0,0

	if matrix[i][j] == matrix[i+1][j+1] and matrix[i+1][j+1] == matrix[i+2][j+2]:
		
		if matrix[i][j] == 'x':
			print("Player 1 wins")
		elif matrix[i][j] == 'o':
			print("Player 2 wins")
		
	else:
		print("No winner")
				

tictactoe_game()

			
		
