
# Ask for month of birth
birthMonth = input('What is your birth month? (1-12)')

# Ask for the day of birth
birthDay = input('Which day of the month you were born?')

# Say the full birth date
print('So you were born on ' + birthDay + '.' + birthMonth)

# Substract birthMonth from birthDay
subNum = int(birthDay) - int(birthMonth)

# Ask for the shoe size
shoeSize = input('What is your shoe size?')

# Add shoeSize to your subNum and present the lucky number to the User
luckyNum = subNum + int(shoeSize)
print('So your lucky number is ' + str(luckyNum) + '.')
