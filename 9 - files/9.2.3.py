def who_is_missing(file_name):
    COMMA = ','
    file = sorted(open(file_name, 'r').read().split(COMMA))
    new_file = open('./found.txt', 'w')
    for index in range(1, len(file) + 1):
        if index != int(file[index - 1]):
            new_file.write(str(index))
            return index

print(who_is_missing("C:/Users/LIAMR/Documents/Adobe/hey.txt"))

"C:/Users/LIAMR/Documents/Adobe/hey.txt"