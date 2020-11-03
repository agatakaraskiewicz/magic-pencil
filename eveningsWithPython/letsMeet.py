from datetime import date

# Ask for name
name = input('What is your name?')

# Say Hello with the name, which was provided
print('Hello ' + name + '!')

# Ask for the fave movie
faveMovie = input('What is your favourite movie?')

# Say that this movie is really nice
print('"' + faveMovie + '"' + ' is a really good movie :)')

# Ask for the birth year
birthYear = input('Which year were you born?')

# Say the age of that person
currentYear = date.today()
print('Currently we are in ' + str(currentYear.year))

age = currentYear.year - int(birthYear)
print('So you must be ' + str(age) + ' years old.')

# Say goodbye
print('It was nice to meet you, ' + name + '. Have a nice day!')