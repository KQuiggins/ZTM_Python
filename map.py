""" def multiplyByTwo(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list """

def multiplyByTwo(item):
    
    return item*2

print(list(map(multiplyByTwo, [2, 4, 6])))