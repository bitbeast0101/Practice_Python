import random
def game():
	count = 0
	number = random.randint(0,11)
	usr_command = "noexit"
	game_continue = ""
	while usr_command == 'noexit':
		guess = int(input("Guess the number: "))
		count += 1 
		if guess > number:
			print(" GUess too high")
		elif guess < number:
			print("guess too low")
		elif guess == number:
			print("exactly right")
			break
		game_continue = input("Y/N: ")
		if game_continue == 'y':
			usr_command = 'noexit'
		else:
			usr_command = 'exit'
			break
	print("Game summary\n")
	print(count)
game()	
			 
