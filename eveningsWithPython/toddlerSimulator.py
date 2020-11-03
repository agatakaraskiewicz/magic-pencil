answer = ''
badWords = ['fuck', 'suck', 'damn']
endWord = 'Because'

while answer.lower() != endWord.lower():
	answer = input('Why?')
	if answer in badWords:
		print('You told me not to use these words!')


print('Good! The end of the suffering of yours!')