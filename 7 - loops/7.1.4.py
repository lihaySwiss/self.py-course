def squared_numbers(start, stop):
    list = []
    while(start<=stop):
        list += [start**2]
        start+=1
    return list

def squared_numbers(start, stop):
    return [i**2 for i in range(start,stop + 1)]

print(squared_numbers(3,5))