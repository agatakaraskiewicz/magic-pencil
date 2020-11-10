from random import randint
"""
1 - Paper
2 - Stone
3 - Scissors

1 beats 2 
2 beats 3
3 beats 1
"""

#1. Create some randomized number (1,3), which will be the comp attack
attack = randint(1,3)

#2. Ask for the RPS input
userAttack = int(input('What is your attack? Input 1 for Paper, 2 for Stone or 3 for Scissors'))

#3. Compare the created values and decide, who won
if userAttack == 1:
	if attack == 1:
		print(f'Tie!')
	elif attack == 2:
		print(f'You won!')
	else:
		print(f'You loose!')
elif userAttack == 2:
	if attack == 2:
		print(f'Tie!')
	elif attack == 3:
		print(f'You won!')
	else:
		print(f'You loose!')
elif userAttack == 3:
	if attack == 3:
		print(f'Tie!')
	elif attack == 1:
		print(f'You won!')
	else:
		print(f'You loose!')
else:
	print('You were supposed to provide 1-3 number... Try again')
