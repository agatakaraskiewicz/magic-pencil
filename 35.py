base_numbers = range(0, 1001)
devisible_numbers = []

for x in base_numbers:
    if x % 3 == 0 or x % 5 == 0: #checks if each of numbers from range is
                                    #devisible by 3 or 5 w/o rest
        devisible_numbers.append(x) #if the condition is True for x, x is added
                                    #to devisible_numbers list
print sum(devisible_numbers)
