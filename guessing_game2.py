import random
def guess2():
	with open('sowpod_dictionary','r') as f:
		data = f.readlines()
	l = len(data)
	print(data,l)		
	word = random.choice(data)
	print(word)
guess2()
	
