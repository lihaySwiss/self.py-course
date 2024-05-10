def format_list(my_list):
    last = my_list[-1]
    my_list = my_list[0:-1:2]
    my_list = str(my_list)[1:-1]
    my_list = my_list.replace("'", "")
    my_list = my_list + ", and " + last
    return my_list
