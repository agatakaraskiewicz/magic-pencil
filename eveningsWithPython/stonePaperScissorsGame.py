from random import randint
"""
1 - Paper
2 - Stone
3 - Scissors

1 beats 2 
2 beats 3
3 beats 1
"""
points = 0
userPoints = 0

howManyWins = int(input('How many wins?'))

#1. Create some randomized number (1,3), which will be the comp attack

#3. Compare the created values and decide, who won
while points < howManyWins and userPoints < howManyWins:
	userAttack = int(input('What is your attack? Input 1 for Paper, 2 for Stone or 3 for Scissors'))
	attack = randint(1,3)
	if userAttack == attack:
		print (f'Tie! No one gets the point!')
		continue
	elif userAttack == 1:
		if attack == 2:
			print(f'You won!')
			userPoints += 1
			continue
		else:
			print(f'You loose!')
			points += 1
			continue
	elif userAttack == 2:
		if attack == 3:
			print(f'You won!')
			userPoints += 1
			continue
		else:
			print(f'You loose!')
			points += 1
			continue
	elif userAttack == 3:
		if attack == 1:
			print(f'You won!')
			userPoints += 1
			continue
		else:
			print(f'You loose!')
			points += 1
			continue
	else:
		print('You were supposed to provide 1-3 number... Try again')

if points > userPoints:
	print('Computer won the battle!')	
else:
	print('You won the battle!')
