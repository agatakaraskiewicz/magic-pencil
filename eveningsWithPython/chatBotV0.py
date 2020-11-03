

# Ask for name and say hello
name = input('What is your name?')
print('Hello ' + name + '!')

# Ask for the age
age = int(input('How old are you?'))

# Answer rearding the provided age
if age > 18:
	electionDone = input('Did you take part in the election?')
elif age == 18:
	print('I wish you luck in further life choices :)')
else:
	voteForWho = input('Who would you like to vote for?')