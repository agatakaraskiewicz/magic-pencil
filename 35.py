base = range (0, 1001)
next = []

for x in base:
    if x % 3 == 0 or x % 5 == 0:
        next.append(x)

print sum (next)
