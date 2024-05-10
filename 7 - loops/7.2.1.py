def is_greater(my_list, n):
    bigger_than_n = []
    for i in range(len(my_list)):
        if(my_list[i]>n):
            bigger_than_n+=[my_list[i]]
    return bigger_than_n