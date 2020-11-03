from random import randint

# Create a random number
luckyNumber = randint(1, 10)
attempts = 1
# Ask for guess
userGuess = int(input('Guess a number between 1 and 10'))

# if the user guesses right away - inform!
if userGuess == luckyNumber:
	print(f'Congrats! You guessed the number and it took only {attempts} attempt!')
else:
	# As long as the guess is not correct - inform and ask again
	while userGuess != luckyNumber:
		print('Not this time')
		print(f'You tried {attempts} time(s)')
		userGuess = int(input('Guess a number between 1 and 10'))
		# Increment the number of attempts taken
		attempts += 1

		#if user finds the number on second or third attempt -inform and break the loop
		if userGuess == luckyNumber:
			print(f'Congrats! You guessed the number and it took only {attempts} attempts!')
			break
		#if no success on all 3 attempts - fail and breake the loop	
		elif userGuess != luckyNumber and attempts == 3:
			print(f'You failed. The lucky number was: {luckyNumber}. Try again.')
			break
		#if no success, but there are still attempts left - continue the loop	
		else:
			continue
	