def count_chars(my_str):
    result = {}
    for i in range(len(my_str)):
        if my_str[i] != ' ':
            if my_str[i] not in result.values():
                result[my_str[i]] = my_str.count(my_str[i])
    return result

print(count_chars('Canada')	)