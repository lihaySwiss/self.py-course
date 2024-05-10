def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    return a + b + c


def fix_age(age):
    if (13 <= age <= 19):
        if (age != 15 and age != 16):
            age = 0
    return age
