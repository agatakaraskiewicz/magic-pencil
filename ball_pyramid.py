"""Small program, which will easly count the amount of balls, you need to build
a pyramid with certain number of them on the side of the base.
It uses command line arguments, so to run it with any number, you have to write

$ python ball_pyramid.py n

where 'n' is your number in base, my dear Agata ;}"""

import sys

side_of_floor = int(sys.argv[1]) #it takes the command line arg ^^
            #it takes 1st arg, because 0 arg is the name of file
            #so it wouldn't work with range(). The same reason is for using
            #int() -> command line args are normally strings, not ints
amount_in_floor = []

for x in range(1, side_of_floor + 1): #adds 1, because range() function doesn't
                                    #count this last number and I want it to be
                                    #comfy for user... I mean... for ME! ;}
    powered = x**2 # counts amount of balls on each floor
    amount_in_floor.append(powered)

sum_of_balls = sum(amount_in_floor)

print "Pyramid, which has {} balls in side of base, has to be build of {} balls.".format(side_of_floor,sum_of_balls)

if sum_of_balls >= 10e5:
    print "It's hella huuuuuge pyramid!"
elif sum_of_balls >= 10e4:
    print "Wow, it's very big thing!"
elif sum_of_balls >= 10e3:
    print "Hmmmm... Quite big ball cone."
elif sum_of_balls >= 10e2:
    print "Oh... A lot of balls!"
else:
    print "Don't waste your time for such small pyramid..."
