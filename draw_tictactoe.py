def tictactoe():
	game = [[0,0,0],
		[0,0,0],
		[0,0,0]]
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
		print(game)
tictactoe()

			
		
