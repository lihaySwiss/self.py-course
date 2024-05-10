def arrow(my_char, max_length):
    pyramid = ""
    for i in range(max_length):
        pyramid += my_char * i
        if(i >= 1):
            pyramid += '\n'
    for i in range (max_length, 0, -1):
        pyramid += my_char * i
        if(i > 1):
            pyramid += '\n'
    return pyramid

def arrow(my_char, max_length):
    return [str(my_char) * i for i in range(max_length) if i >=1]

print(arrow('*', 5))