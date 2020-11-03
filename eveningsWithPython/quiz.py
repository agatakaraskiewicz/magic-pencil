points = 0

# question 1
nobelPrize = 'Olga Tokarczuk'
secondNobelPrize = 'Peter Handke'
alternativeNobelPrize = 'Tokarczuk'
secondAltNobelPrize = 'Handke'

userAnswer = input('Who got the literature Nobel prize in 2019?')

if userAnswer == nobelPrize or userAnswer == secondNobelPrize or userAnswer == alternativeNobelPrize or userAnswer == secondAltNobelPrize:
	print('Correct!')
	points += 1
else:
	print('Nope. Correct answers are: ' + nobelPrize + ' or ' + secondNobelPrize + ' or ' + alternativeNobelPrize + ' or ' + secondAltNobelPrize)


# question 2
bestBeer = 'Tyskie'
secondBestBeer = 'Okocim'
thirdBestBeer = 'Warka'

userAnswer2 = input('What is the best Polish beer?')

if userAnswer2 == bestBeer or userAnswer2 == secondBestBeer or userAnswer2 == thirdBestBeer:
	print('Correct')
	points += 1
else:
	print('Nope. Correct answers are: ' + bestBeer + ' or ' + secondBestBeer + ' or ' + thirdBestBeer)


# question 3
bestPlant = 'Monstera'
secondBestPlant = 'Epi'
thirdBestPlant = 'Kroton'

userAnswer3 = input('What is the most fashionable plant ever?')

if userAnswer3 == bestPlant or userAnswer3 == secondBestPlant or userAnswer3 == thirdBestPlant:
	print('Correct')
	points += 1
else:
	print('Nope. Correct answers are: ' + bestPlant + ' or ' + secondBestPlant + ' or ' + thirdBestPlant)

print('Here are the points you got: ' + str(points))		
