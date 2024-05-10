def numbers_letters_count(my_str):
    output_list = [0,0]
    for i in range(len(my_str)):
        if(my_str[i].isnumeric()):
            output_list[0] += 1
        else:
            output_list[1] += 1
    return output_list

numbers_letters_count('Python 3.6.3')