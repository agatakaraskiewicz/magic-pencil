
# question 1
noblePrize = 'Olga Tokarczuk'
secondNoblePrize = 'Peter Handke'
userAnswer = input('Who got the literature Noble prize in 2019?')

if userAnswer in noblePrize or userAnswer in secondNoblePrize:
	print('Correct!')
else:
	print('Nope. It was ' + noblePrize + ' and ' + secondNoblePrize)