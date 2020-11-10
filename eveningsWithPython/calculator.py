def runFunction():
	def calculate(first, second, math):
		if math == 'sum':
			return first + second
		elif math == 'minus':
			return first - second
		elif math == 'times':
			return first * second
		elif math == 'divide':
			return first / second
		else:
			print('There is no such operation. Try again')

	firstNmbr = int(input('What is the first number?'))
	secondNmbr = int(input('What is the second number?'))

	mathOperation = input('What do I do with them? (sum, minus, times, divide)')

	result = calculate(firstNmbr, secondNmbr, mathOperation)

	print('The result is: ' + str(result))
	
runFunction()
runFunction()
runFunction()	