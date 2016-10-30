import sys

equat = sys.argv[1:]
joined = ''.join(equat)

if joined[-1] in '0123456789':
    joined = joined + '.0'
elif joined[-1] == ')':
    if joined[-2] in '0123456789':
        joined = joined[:-1] + '.0' + joined[-1]
    else:
        print 'WTF?! Check, if you wrote everything correctly!'
else:
    print 'WTF?! Check, if you wrote everything correctly!'

count = eval(joined)

print count
