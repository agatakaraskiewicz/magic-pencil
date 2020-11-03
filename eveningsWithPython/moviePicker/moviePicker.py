

moviePositive = input('Do you fancy watching a movie?')
if moviePositive == 'Yes':
	polishMovie = input('Should it be a Polish movie?')
	if polishMovie == 'Yes':
		historicMovie = input('Historic one?')
		if historicMovie == 'Yes':
			print('You should watch "Legiony"')
		else:
			print('You should watch "Boże Ciało"')
	else:
		superheroMovie = input('Do you like Superhero Movies?')
		if superheroMovie == 'Yes':
			print('You should watch "Joker"')
		else:
			asianMovie = input('Should it be an Asian movie then?')
			if asianMovie == 'Yes':
				print('You should watch "Parasite"')
			else:
				print('You should watch "Portret kobiety w ogniu"')					
else:
	print('Then why the hell do you bother me???')