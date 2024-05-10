def are_lists_equal(list1, list2):
    """
    Function will tell if two given lists have the same items
    :param list1: first list
    :param list2: second list
    :return: True/ False
    """
    if(set(list1) == set(list2)):
        return True
    return False
