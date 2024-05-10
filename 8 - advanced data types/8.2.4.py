def sort_anagrams(list_of_strings):
    new_list = []
    for string in list_of_strings:
        for other_string in list_of_strings:
            if sorted(other_string) == sorted(string):
                new_list.append(other_string)
                break
            else:
                new_list.append([string])
                break
            break

    return new_list

def sort_anagrams(list_of_strings):
    new_list = []
    for i in range(len(list_of_strings) - 1):
        for j in range(len(list_of_strings) - 1):
            if sorted(list_of_strings[i]) == sorted(list_of_strings[j]):
                new_list.append(list_of_strings[j])
                break
            else:
                new_list.append([list_of_strings[j]])
                break
    return new_list

print(sort_anagrams(['abc', 'bcd', 'cda']))
print(sort_anagrams(['abc', 'bca', 'cba']))
print(sort_anagrams(['abc', 'bcd', 'cba']))