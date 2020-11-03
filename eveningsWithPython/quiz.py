
# question 1
nobelPrize = 'Olga Tokarczuk'
secondNobelPrize = 'Peter Handke'
userAnswer = input('Who got the literature Nobel prize in 2019?')

if userAnswer in nobelPrize or userAnswer in secondNobelPrize:
	print('Correct!')
else:
	print('Nope. It was ' + nobelPrize + ' and ' + secondNobelPrize)