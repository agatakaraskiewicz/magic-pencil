# it joins list elements into a simple sentence


def makeItSentence(x):
    sentence = ''
    for i in x:
        if x.index(str(i)) < x.index(x[-2]):
            sentence = sentence + str(i) + ', '
        elif x.index(str(i)) < x.index(x[-1]):
            sentence = sentence + str(i) + ' '
        else:
            sentence = sentence + 'and ' + str(i)
    return sentence        

spam = ['apples', 'bananas', 'tofu', 'cats']
print (makeItSentence(spam))