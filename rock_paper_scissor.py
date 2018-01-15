def game():
	player_1 = input("Enter player 1 input: ")
	
	while player_1 == 'rock' or 'paper' or 'scissor':
		if player_1 == 'rock' or 'paper' or 'scissor':			
			break	
		else:
			print("enter valid input\n")
			player_1 = input("Enter player 1 input: ")
			
	player_2 = input("Enter player 2 input: ")
	while player_2 == 'rock' or 'paper' or 'scissor':
		if player_2 == 'rock' or 'paper' or 'scissor':			
			break	
		else:
			print("enter valid input\n")
			player_2 = input("Enter player_2 input: ")

	if player_1 == player_2:
		print("clash\n No winner")
	elif player_1 == 'rock' and player_2 == 'paper':
		print("player_2 wins") 
	elif player_1 == 'rock' and player_2 == 'scissor':
		print("player_1 wins") 
	elif player_1 == 'paper' and player_2 == 'rock':
		print("player_1 wins")
	elif player_1 == 'paper' and player_2 == 'scissor':
		print("player_2 wins")
	elif player_1 == 'scissor' and player_2 == 'rock':
		print("player_2 wins")
	elif player_1 == 'scissor' and player_2 == 'paper':
		print("player_1 wins")	
			
game()
		
		
			
