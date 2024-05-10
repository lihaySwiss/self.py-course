def seven_boom(end_number):
    numbers_list = []
    for i in range(end_number+1):
        if(i%7 == 0):
            numbers_list.append('BOOM')
        elif('7' in str(i)):
            numbers_list.append('BOOM')
        else:
            numbers_list.append(i)

    return numbers_list.append('BOOM') if i%7==0 else numbers_list.append(i)


#Second way of writing it
def seven_boom(end_number):
    return ['BOOM' if digit % 7 == 0 or '7' in str(digit) else digit for digit in range(end_number+1)]


print(seven_boom(8))
