def shift_left(my_list):
    """
    Function will shift list objects one step to left
    :param my_list: list parameter
    :type my_list: list
    :return: list with one shift to left
    """
    temp = my_list[0] #temporary variable
    my_list[0:-1:] = my_list[1::]
    my_list[-1] = temp
    return my_list