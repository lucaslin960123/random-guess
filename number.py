import random
r = random.randint(1,100)
while True:
	a = int(input('Guess a random number:'))
	if a == r:
		print('You are right!')
		break
	elif a > r:
		print('Guess it smaller!')
	elif a < r:
		print('Guess it bigger!')