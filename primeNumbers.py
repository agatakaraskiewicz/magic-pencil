#list of a numbers from range 1000 - 10000
numbers = list(range(1000, 10000)) 

#little loop for checking, if there is any rest from dividing by prime numbers between 2 and 20. If the condition gives True - it should be a prime number... I guess...
for number in numbers:
    if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0 and number % 9 != 0 and number % 11 != 0 and number % 13 != 0 and number % 17 != 0 and number % 19 != 0:
        print number
        
#alredy know, that it's wrong and not enough