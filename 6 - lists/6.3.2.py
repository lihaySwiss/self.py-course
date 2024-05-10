def longest(my_list):
    """
    Function will print longest item in given list
    :param my_list: given list
    :return: longest string
    """
    my_list.sort(key=len)
    return my_list[-1]

longest(['a', 'b', 'c', 'abc', 'typewriter', 'd'])
longest(['a', 'b', 'c', 'abcdefghij', 'typewrit', 'd'])