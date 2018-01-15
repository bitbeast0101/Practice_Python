import random
def hangman2():
	print("Welcome to Hangman","\n Only CAPS")
	word = hangman1()
	word = list(word)
	
	duplicate = word
	length = len(word)	
	usr_str = [None]*(length)
	usr_str[-1] = '\n'
	
	print(("_")*(length))
	count = 0
	
	flag = 0
	i = 0
	while flag == 0:
		guess = input("Enter your guess letter:")
		if guess in usr_str:
			print("Already guessed this letter")
			continue
		while guess in word:
			if guess == word[i]:
				usr_str[i] = guess
				word[i] = '*'
							
			i += 1
		i = 0
		if guess not in duplicate:
			print("Wrong guess! Try Again!")
		
		print(" "*i+guess+" "*((length - 1)-i))		
		print(word)
		print(usr_str)
		print(("_"+" ")*(length-1))	
			
		count += 1
		if usr_str == duplicate:
			flag = 1



def hangman1():
	with open('sowpod_dictionary','r') as f:
		data = f.readlines()
	
			
	word = random.choice(data)
	print(word)
	return word


hangman2()

	
