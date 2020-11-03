# Ask for name and say hello
name = input('What is your name?')
print('Hello ' + name + '!')

# Ask if the user is happy and regarding the answer provide some life advice
happiness = input('Are you happy?')
if happiness == 'Yes':
	enhanceLife = input('Do you want to make your life even better?')
	if enhanceLife == 'Yes':
		print('You should invest in the new cryptocurrency - it will be a hit!')
	else:
		print('Oh you lazy-lazy! Better put yourself together and start your own company!')
else:
	print('You should start a company! It will make you happy')	

# Say goodbye
print('Hope I helped! Have a nice one!')	