import sys

equat = sys.argv[1:]
join = ''.join(equat)

if join[-1] == '0':
    join = join + '.0'
elif join[-1] == '1':
    join = join + '.0'
elif join[-1] == '2':
    join = join + '.0'
elif join[-1] == '3':
    join = join + '.0'
elif join[-1] == '4':
    join = join + '.0'
elif join[-1] == '5':
    join = join + '.0'
elif join[-1] == '6':
    join = join + '.0'
elif join[-1] == '7':
    join = join + '.0'
elif join[-1] == '8':
    join = join + '.0'
elif join[-1] == '9':
    join = join + '.0'
elif join[-1] == ')':
    if join[-2] == '0':
        join = join + '.0'
    elif join[-2] == '1':
        join = join + '.0'
    elif join[-2] == '2':
        join = join + '.0'
    elif join[-2] == '3':
        join = join + '.0'
    elif join[-2] == '4':
        join = join + '.0'
    elif join[-2] == '5':
        join = join + '.0'
    elif join[-2] == '6':
        join = join + '.0'
    elif join[-2] == '7':
        join = join + '.0'
    elif join[-2] == '8':
        join = join + '.0'
    elif join[-2] == '9':
        join = join + '.0'
    else:
        print 'WTF?! Check, if you wrote everything correctly! '
else:
    print 'WTF?! Check, if you wrote everything correctly! '
    
count = eval(join)

print count
