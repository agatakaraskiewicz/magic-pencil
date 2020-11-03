
# question 1
nobelPrize = 'Olga Tokarczuk'
secondNobelPrize = 'Peter Handke'
alternativeNobelPrize = 'Tokarczuk'
secondAltNobelPrize = 'Handke'
userAnswer = input('Who got the literature Nobel prize in 2019?')

if userAnswer == nobelPrize or userAnswer == secondNobelPrize or userAnswer == alternativeNobelPrize or userAnswer == secondAltNobelPrize:
	print('Correct!')
else:
	print('Nope. Correct answers are: ' + nobelPrize + ' or ' + secondNobelPrize + ' or ' + alternativeNobelPrize + ' or ' + secondAltNobelPrize)
	