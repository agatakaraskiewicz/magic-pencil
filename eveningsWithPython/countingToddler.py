
startNumber = int(input('What is the beginning number?'))
endNumber = int(input('What is the end of our counting?'))

if endNumber > startNumber:
	while startNumber <= endNumber:
		print(startNumber)
		startNumber += 1
else:
	print('Not possible! It would be reverse... I cannot do that yet!')