"""Little calculator of factorials. In line 5 it takes a number as an input and then
it counts a factorial of it. Function outputs 1 for     number <= 1 
-> for numbers under 0 too..."""

number = int(raw_input("Number:"))

def factorial(x):
    if x == 1 or x == 0:
        return 1
    elif x < 0:
        print "Number below 0. Try again." 
        x = int(raw_input("Number:"))
        return factorial(x)
    else:
        return x * factorial(x - 1)
        
print factorial(number)
