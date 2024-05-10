def inverse_dict(my_dict):
    result = {}
    for i, j in sorted(my_dict.items()):
        result[j] = result.get(j, []) + [i]
    return result

print(inverse_dict({'b': 'd', 'a': 'd', 'c': 'd'}))
print(inverse_dict({'%': '4', 'dd': '5', '!': '5', 'bb': 'cd', 'ab': 'cd', 'cc': 'dd', '$': '5'}))