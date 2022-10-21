my_list = ['a', 'b', 'c', 'd', 'm', 'n', 'n']

duplicates = []

for char in my_list:
    if my_list.count(char) > 1:
        duplicates.append(char)

print(duplicates)