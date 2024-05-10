file = open(input("Enter file path: "), 'r')
method = input("Enter a task: ")

if method == 'sort':
    list = []
    content = file.read().replace('\n', ' ').split(' ')
    for word in content:
        if(word not in list and word != ''):
            list.append(word)
    list = sorted(list)
    print(list)

elif method == 'rev':
    content = file.read().split('\n')
    for line in content:
        for char in line[::-1]:
            print(char, end = "")
        print(' ', end = "")

elif method == 'last':
    content = file.read().split('\n')
    n = int(input("Enter a number: "))
    while n != 0:
        print(content[len(content) - n])
        n -= 1

"""C:\sampleFile.txt"""