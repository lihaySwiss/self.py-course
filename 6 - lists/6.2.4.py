def extend_list_x(list_x, list_y):
    """
    Function will put list_y at the beginning of list_x
    :param list_x: list to be extended
    :param list_y: extended data
    :return: extended list
    :rtype: array
    """
    list_x = [*list_y, *list_x]
    return list_x

print(extend_list_x([4, 5, 6],[1, 2, 3]))