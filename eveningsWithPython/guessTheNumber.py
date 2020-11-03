from random import randint

luckyNumber = randint(0, 10)
attempts = 1
userGuess = int(input('Guess a number between 1 and 10'))

if userGuess == luckyNumber:
	print(f'Congrats! You guessed the number and it took only {attempts} attempt!')
else:
	while userGuess != luckyNumber and attempts < 3:
		print('Not this time')
		print(f'You tried {attempts} times')
		userGuess = int(input('Guess a number between 1 and 10'))
		attempts += 1

if attempts == 3:
	print('You failed. Try again.')
else:
	print(f'Congrats! You guessed the number and it took only {attempts} attempts!')	


