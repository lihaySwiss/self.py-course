def mult_tuple(tuple1, tuple2):
    list1 = []
    for i in range(len(tuple1)):
        for j in range(len(tuple2)):
            list1 += [(tuple1[i], tuple2[j])]
    for i in range(len(tuple2)):
        for j in range(len(tuple1)):
            list1 += [(tuple2[i], tuple1[j])]
    return tuple(list1)

def mult_tuple(tuple1, tuple2):
    return tuple([(i, j) for i in tuple1 for j in tuple2] + [(i, j) for i in tuple2 for j in tuple1])
        

print(mult_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9), (10, 11, 12, 13)))
