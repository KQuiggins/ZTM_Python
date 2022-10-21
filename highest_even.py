def highest_even(li):
    evens = []
    highest = 0
    
    for num in li:
        if num % 2 == 0:
            evens.append(num)
    
    for i in evens:
        if i > highest:
            highest = i
    return highest

print(highest_even([6, 5, 8, 10, 13]))
