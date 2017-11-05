"""Little calculator of factorials. In line 5 it takes a number as an input and then
it counts a factorial of it. Function outputs 1 for     number <= 1 
-> for numbers under 0 too..."""

number = int(raw_input("Number:"))

def factorial(x):
    total = 1
    while x > 0:
        total = total * x
        x = x-1
    
    print "Factorial of that number is:", total
    
factorial(number)