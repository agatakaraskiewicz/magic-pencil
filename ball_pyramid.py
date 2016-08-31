from math import pow

side_of_floor = range(1, 18) #1rst floor == 17 balls at side; on top is just 1
amount_in_floor = []

for x in side_of_floor:
    powered = int(pow(x,2)) # counts amount of balls on each floor
    amount_in_floor.append(powered)

sum_of_balls = sum(amount_in_floor)

print "In this pyramid is {} balls.".format(sum_of_balls)

if sum_of_balls == 1785:
    print "And this picture was true!"
else:
    print "And this picture was fake!"
