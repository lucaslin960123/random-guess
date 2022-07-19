import random
count = 0
r = random.randint(1,100)
while True:
	a = int(input('Guess a random number:'))
	count += 1
	if a == r:
		print('You are right!')
		print('Total count = ',count)
		break
	elif a > r:
		print('Guess it smaller!')
		print('This is your ',count,'time to guess')
	elif a < r:
		print('Guess it bigger!')
		print('This is your ',count,'time to guess')