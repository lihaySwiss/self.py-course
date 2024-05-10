def sequence_del(my_str):
    i = 1
    while i < len(my_str):
        for j in range(i, len(my_str)):
            if my_str[j - 1] == my_str[j]:
               my_str = my_str[:j - 1] + my_str[j:]
        i += 1
    return my_str

print(sequence_del('pyyyyyyttthhhooonnnn'))
print(sequence_del('AAAAAAAbbbbb!!BBBBBaaaaa'))
print(sequence_del(''))