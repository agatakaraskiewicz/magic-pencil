from random import randint

luckyNumber = randint(0, 10)
attempts = 1
userGuess = int(input('Guess a number between 1 and 10'))

if userGuess == luckyNumber:
	print(f'Congrats! you guessed the number and it took only {attempts} attempt!')
else:
	while userGuess != luckyNumber:
		print('not this time')
		attempts += 1
		print(f'You tried {attempts} times')
		print(luckyNumber)
		userGuess = int(input('Guess a number between 1 and 10'))

print(f'Congrats! you guessed the number and it took only {attempts} attempts!')	


