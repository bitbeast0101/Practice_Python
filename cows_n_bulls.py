import random
answer = str(random.randint(1000,9999))
def game():
	
	answer_list = list(answer)
	print(answer_list)
	continue_ = 'y'
	cows = 0
	bulls = 0
	no_of_guesses = 0
	while continue_== 'y':
		guess = input("Enter your 4 digit guess:")
		guess_list = list(guess)
		print(guess_list)
		if guess_list[0] in answer_list:
			if guess_list[0] == answer_list[0]:
				cows += 1
			else:
				bulls += 1
		if guess_list[1] in answer_list:
			if guess_list[1] == answer_list[1]:
				cows += 1
			else:
				bulls += 1
		if guess_list[2] in answer_list:
			if guess_list[2] == answer_list[2]:
				cows += 1
			else:
				bulls += 1
		if guess_list[3] in answer_list:
			if guess_list[3] == answer_list[3]:
				cows += 1
			else:
				bulls += 1
		print("cows : {} , bulls = {}".format(cows,bulls))
		cows = 0
		bulls = 0	
		continue_ = input("y/n:")
		if continue_ == 'y':
			no_of_guesses += 1
		else:
			print(no_of_guesses)
		
game()
		
		
