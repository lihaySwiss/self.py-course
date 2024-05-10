def last_early(my_str):
    my_str = my_str.lower()
    if(my_str.find(my_str[-1]) < len(my_str)-1):
        return True
    else:
        return False
